"""Check task Markdown, model parity, evidence freshness and forbidden publication paths."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml  # Existing workstation PyYAML; no installer is invoked.

ROOT=Path(__file__).resolve().parents[1]
VAULT=ROOT/'Structure DB Obsidian'


def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').strip()


def changed_paths():
    changed=git('diff','--name-only','origin/main').splitlines()
    untracked=git('ls-files','--others','--exclude-standard').splitlines()
    return sorted(set(changed+untracked))


def without_fences(text):
    output=[];fence=None
    for line in text.splitlines():
        m=re.match(r'^\s*(`{3,}|~{3,})',line)
        if m:
            marker=m.group(1)[0]
            if fence is None:fence=marker
            elif fence==marker:fence=None
            continue
        if fence is None:output.append(line)
    return '\n'.join(output),fence


def main():
    errors=[];paths=changed_paths();markdown=[p for p in paths if p.endswith('.md')]
    by_name={}
    for file in VAULT.rglob('*.md'):by_name.setdefault(file.stem,[]).append(file)
    frontmatter=0
    for name in markdown:
        file=ROOT/name;text=file.read_text(encoding='utf-8');body,fence=without_fences(text)
        if fence:errors.append(name+': unclosed fence')
        if file.is_relative_to(VAULT):
            if not text.startswith('---\n'):errors.append(name+': no frontmatter');continue
            try:
                data=yaml.safe_load(text.split('---',2)[1]);frontmatter+=1
                for field in ['id','project','type','status','owner','updated','tags','source_of_truth']:
                    if field not in data:errors.append(name+': missing '+field)
                if not (file.parent/data['source_of_truth']).resolve().exists():errors.append(name+': source_of_truth missing')
            except (KeyError,yaml.YAMLError,TypeError) as exc:errors.append(name+': frontmatter '+str(exc))
        for target in re.findall(r'\[\[([^\]]+)\]\]',body):
            target=target.split('|')[0].split('#')[0]
            if not target or target.startswith('<'):continue
            candidates=by_name.get(Path(target).name,[])
            if not candidates:errors.append(name+': unresolved wiki '+target)
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\n)]+)\)',body):
            target=target.strip().strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
            if '<' in target or '...' in target:continue  # literal template placeholders, not project links
            target=unquote(target.split('#')[0])
            if target and not (file.parent/target).resolve().exists():errors.append(name+': missing local link '+target)
    dictionary=(VAULT/'03_Data/Data_Dictionary_Draft.md').read_text(encoding='utf-8')
    expected=set(re.findall(r'^\| `([a-z_]+)` \|',dictionary,re.M))
    erd=(VAULT/'03_Data/ERD_Draft.md').read_text(encoding='utf-8')
    erd_names={v.lower() for line in erd.splitlines() if '--' in line and ':' in line for v in re.findall(r'\b[A-Z][A-Z_]+\b',line)}
    contract=json.loads((ROOT/'database/schema_contract.json').read_text(encoding='utf-8'))
    inventory=json.loads((ROOT/'database/evidence/schema_inventory.json').read_text(encoding='utf-8'))
    if expected!=erd_names or expected!=set(contract['logical_tables']) or expected!=set(inventory['tables']) or len(expected)!=47:
        errors.append('ERD/dictionary/SQL manifest/live inventory parity')
    results=json.loads((ROOT/'database/evidence/test_results.json').read_text(encoding='utf-8'))
    for name,digest in results['source_file_sha256'].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:errors.append('Stale test source evidence: '+name)
    for item in inventory['migrations']:
        if hashlib.sha256((ROOT/'database/migrations'/item['name']).read_bytes()).hexdigest()!=item['sha256']:errors.append('Stale migration evidence: '+item['name'])
    for name in paths:
        if name.startswith('.local/') or Path(name).suffix.lower() in {'.jsonl','.csv','.dump','.backup','.env'}:
            errors.append('Forbidden publication path: '+name)
        if (ROOT/name).is_file():
            text=(ROOT/name).read_text(encoding='utf-8')
            for pattern in [r'gh[pousr]_[A-Za-z0-9]{20,}',r'github_pat_[A-Za-z0-9_]{20,}',r'sk-[A-Za-z0-9]{24,}',r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----']:
                if re.search(pattern,text):errors.append('Possible secret pattern: '+name)
    receipt='Structure DB Obsidian/08_Operations/Receipts/2026-11-10_201028_DPT-PLAN-001_P1_Planning.md'
    retained=[receipt,*['Structure DB Obsidian/03_Data/'+v for v in ['P1_Data_Profiling_Findings.md','P1_Source_to_Canonical_Mapping.md','P1_Data_Conflict_Matrix.md']]]
    for name in retained:
        if git('hash-object',name)!=git('rev-parse','origin/main:'+name):errors.append('Historical evidence changed: '+name)
    # OD approval rows must remain identical in log and planning spec.
    rows=[]
    for name in ['08_Operations/Decision_Log.md','07_Delivery/Planning_PRs/P1_Data_Foundation_Plan.md']:
        text=(VAULT/name).read_text(encoding='utf-8')
        rows.append([line for line in text.splitlines() if re.match(r'^\| OD-0[1-6] \|',line) and 'APPROVED' in line])
    if rows[0]!=rows[1] or len(rows[0])!=6:errors.append('Owner decision row parity')
    subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
    result={'task':'IMP-P1-01','markdown_files':len(markdown),'parsed_frontmatters':frontmatter,'logical_table_parity':len(expected),
            'owner_decisions_unchanged_matching':len(rows[0]),'secret_pattern_candidates':sum('secret pattern' in e for e in errors),
            'historical_evidence_hashes_unchanged':not any('Historical evidence' in e for e in errors),'errors':errors,
            'limits':['No Mermaid rendering','Common secret patterns/path scan only; not a comprehensive security audit','External web URLs not re-fetched by this local link check'],
            'changed_paths':paths}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if not errors:
        (ROOT/'database/evidence/documentation_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return bool(errors)


if __name__=='__main__':sys.exit(main())
