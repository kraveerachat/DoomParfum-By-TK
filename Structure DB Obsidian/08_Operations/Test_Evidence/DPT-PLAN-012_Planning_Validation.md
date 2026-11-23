---
id: DPT-PLAN-012-VALIDATION
project: DoomParfum By TK
type: validation_protocol
status: proposed
owner: human-owner
updated: 2026-11-23
tags: [doomparfum, validation, documentation]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# DPT-PLAN-012 planning validation protocol

This is documentation-only verification. It does not execute frontend, DB, Docker or matching tests. Run the Python block below from the task worktree by extracting its fenced text and executing with `__file__` pointing to this Markdown file. Python 3 and the existing PyYAML installation are required; install nothing. The wrapper runs the unchanged `database/validate_docs.py` in both supported modes and suppresses only its historical evidence-file writes. Its raw results remain FAIL if legacy findings exist. The separate scoped result accounts for inherited findings against exact `origin/main` text and existing JSON targets, validates new content and preserves old bodies/source/receipts.

Output: sibling `DPT-PLAN-012_Planning_Validation.json`, including exact changed paths, bounded scan results, inherited findings and contrast values. That JSON is not a runtime PASS or exhaustive secret clearance. Rerun after final metadata edits; do not modify the validator to obtain a green result. A generated JSON file cannot hash itself; commit SHA binds the final tree. Record validation source hashes separately from final-containing commit.

```python
from pathlib import Path
import contextlib, io, json, re, runpy, subprocess, sys, hashlib
import yaml

root = Path.cwd()
vault = root / 'Structure DB Obsidian'
base = '03e2ab6080373033c02afc7ada7be2ceab5f24e2'
def git(*args):
    return subprocess.check_output(['git', '-c', 'core.quotePath=false', *args], cwd=root, stderr=subprocess.DEVNULL).decode('utf-8')

paths = sorted(set(git('diff', '--name-only', '-z', 'origin/main').split('\0') + git('ls-files', '--others', '--exclude-standard', '-z').split('\0')) - {''})
stock = []
old_write, old_check, old_run = Path.write_text, subprocess.check_output, subprocess.run
def no_legacy_write(p, data, *args, **kwargs):
    if p.parent == root / 'database/evidence' and p.name.endswith('documentation_checks.json'):
        return len(data)
    raise RuntimeError('Unexpected validator write')
def quiet_check(*args, **kwargs):
    kwargs.setdefault('stderr', subprocess.DEVNULL)
    return old_check(*args, **kwargs)
def quiet_run(*args, **kwargs):
    kwargs.setdefault('stderr', subprocess.DEVNULL)
    return old_run(*args, **kwargs)
try:
    Path.write_text, subprocess.check_output, subprocess.run = no_legacy_write, quiet_check, quiet_run
    for mode in ['IMP-P1-01', 'IMP-P1-02']:
        captured = io.StringIO()
        sys.argv = ['database/validate_docs.py', '--task', mode]
        try:
            with contextlib.redirect_stdout(captured):
                runpy.run_path(str(root / 'database/validate_docs.py'), run_name='__main__')
            code = 0
        except SystemExit as exc:
            code = int(exc.code or 0)
        result = json.loads(captured.getvalue())
        stock.append({'mode': mode, 'exit': code, 'markdown_files': result['markdown_files'], 'frontmatters': result['parsed_frontmatters'], 'logical_table_parity': result['logical_table_parity'], 'errors': result['errors']})
finally:
    Path.write_text, subprocess.check_output, subprocess.run = old_write, old_check, old_run

all_files = [p for p in vault.rglob('*') if p.is_file()]
names = {p.name for p in all_files}
stems = {p.stem for p in all_files if p.suffix == '.md'}
inherited, unexplained = [], []
for message in sorted({e for s in stock for e in s['errors']}):
    if message.startswith('Stale test source evidence: '):
        source = message.removeprefix('Stale test source evidence: ')
        if git('hash-object', source).strip() == git('rev-parse', base + ':' + source).strip():
            inherited.append({'finding': message, 'classification': 'pre-existing-source-evidence-mismatch', 'source_blob_unchanged': True})
            continue
    name, _, detail = message.partition(': ')
    try:
        prior = git('show', base + ':' + name)
    except subprocess.CalledProcessError:
        prior = ''
    if detail.startswith('unresolved wiki '):
        target = detail.removeprefix('unresolved wiki ')
        if target in names and ('[[' + target) in prior:
            inherited.append({'finding': message, 'classification': 'legacy-md-only-link-resolver', 'target_exists': True})
            continue
    if detail == 'missing owner' and name.endswith('/Tool_Usage_Log.md') and prior.startswith('---'):
        if 'owner' not in yaml.safe_load(prior.split('---', 2)[1]):
            inherited.append({'finding': message, 'classification': 'pre-existing-frontmatter'})
            continue
    unexplained.append(message)

failures = []
markdown_count = 0
for name in paths:
    p = root / name
    if p.suffix not in {'.md', '.json'} or (name != 'PRODUCT.md' and not name.startswith('Structure DB Obsidian/')):
        failures.append('Out-of-scope path: ' + name)
    if p.suffix != '.md':
        continue
    markdown_count += 1
    text = p.read_text(encoding='utf-8')
    if p.is_relative_to(vault):
        if not text.startswith('---\n'):
            failures.append('Missing frontmatter: ' + name)
            continue
        data = yaml.safe_load(text.split('---', 2)[1])
        for field in ['id', 'project', 'type', 'status', 'owner', 'updated', 'tags', 'source_of_truth']:
            if field not in data and not (field == 'owner' and name.endswith('/Tool_Usage_Log.md')):
                failures.append('Missing field ' + field + ': ' + name)
        if not (p.parent / data['source_of_truth']).resolve().exists():
            failures.append('Bad source_of_truth: ' + name)
    fences = re.findall(r'^```', text, re.M)
    if len(fences) % 2:
        failures.append('Unclosed fence: ' + name)
    body = re.sub(r'```[\s\S]*?```', '', text)
    for target in re.findall(r'\[\[([^\]]+)\]\]', body):
        target = target.split('|')[0].split('#')[0]
        if Path(target).name not in names and Path(target).name not in stems:
            failures.append('Unresolved wiki: ' + name + ': ' + target)
    for pattern in [r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}', r'sk-[A-Za-z0-9]{24,}', r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----', r'[A-Za-z]:[\\/]Users[\\/]']:
        # Public-safe scan covers added/new text, without republishing matched data.
        try:
            previous = git('show', base + ':' + name).replace('\r\n', '\n')
        except subprocess.CalledProcessError:
            previous = ''
        added = text[len(previous):] if previous and text.startswith(previous) else text
        if re.search(pattern, added):
            failures.append('Sensitive-pattern candidate: ' + name)

protected = git('diff', '--name-only', base, '--', 'database', 'matching_math', 'Structure DB Obsidian/04_Matching', 'Structure DB Obsidian/08_Operations/Receipts').splitlines()
old_receipt_edits = [p for p in protected if p.startswith('Structure DB Obsidian/08_Operations/Receipts/') and not 'DPT-PLAN-012' in p]
if old_receipt_edits or any(not p.startswith('Structure DB Obsidian/08_Operations/Receipts/') for p in protected):
    failures.append('Protected source/history changed')
history_paths = [p for p in paths if p in git('ls-tree', '-r', '--name-only', base).splitlines()]
for name in history_paths:
    prior = git('show', base + ':' + name).replace('\r\n', '\n')
    if not (root / name).read_text(encoding='utf-8').startswith(prior):
        failures.append('Existing body not preserved as prefix: ' + name)
matrix = (vault / '05_UX/Luxury_Reference_Research_Matrix.md').read_text(encoding='utf-8')
ids = sorted(set(re.findall(r'^\| ([PF]\d{2}) ', matrix, re.M)))
expected = ['P%02d' % n for n in range(1, 11)] + ['F%02d' % n for n in range(1, 11)]
if set(ids) != set(expected):
    failures.append('Reference coverage not exactly twenty IDs')
routes = (vault / '05_UX/Luxury_Routes_and_Wireframes.md').read_text(encoding='utf-8')
route_rows = re.findall(r'^\| `(/[^`]*?)` \|', routes, re.M)
if set(route_rows) != {'/', '/explore', '/perfume/[slug]', '/notes', '/about'}:
    failures.append('Route contract coverage mismatch')
colors = {'paper':'F7F5F0','white':'FFFFFF','ink':'161719','secondary':'5C5A55','gold':'AD9361','gold-readable':'75613A','navy':'14253D','divider':'DDD9D0','control-border':'817B70','error':'9A302C','success':'365E47'}
def luminance(h):
    v = [int(h[i:i+2],16)/255 for i in (0,2,4)]
    v = [x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v]
    return sum(a*b for a,b in zip(v,[.2126,.7152,.0722]))
pairs = []
for fg, bg, threshold in [('ink','paper',4.5),('secondary','paper',4.5),('gold-readable','paper',4.5),('paper','navy',4.5),('paper','ink',4.5),('control-border','paper',3),('control-border','white',3),('error','paper',4.5),('success','paper',4.5),('gold-readable','white',4.5),('gold','paper',None),('gold','white',None),('divider','paper',None)]:
    low,high = sorted([luminance(colors[fg]),luminance(colors[bg])])
    ratio = (high+.05)/(low+.05)
    pairs.append({'foreground':fg,'background':bg,'ratio':round(ratio,6),'threshold':threshold,'role':'decorative-only' if threshold is None else 'functional'})
    if threshold is not None and ratio < threshold:
        failures.append('Contrast below threshold: '+fg+'/'+bg)
diff = subprocess.run(['git','diff','--check'], cwd=root, capture_output=True, text=True)
if diff.returncode:
    failures.append('git diff --check failed')
record = {'task':'DPT-PLAN-012','base_sha':base,'scope':'documentation-only','stock_validator_results':stock,'legacy_findings_accounted':inherited,'unexplained_stock_findings':unexplained,'scoped_failures':failures,'scoped_result':'PASS' if not failures and not unexplained else 'FAIL','changed_markdown':markdown_count,'changed_paths':paths,'reference_ids':ids,'route_types':route_rows,'contrast_pairs':pairs,'diff_check_exit':diff.returncode,'existing_bodies_preserved':not any('prefix' in f for f in failures),'limits':['Stock validator retains legacy failures; no validator or historical evidence rewritten','Pattern scan only, not exhaustive secret/legal clearance','Reference captures are session evidence, not committed goldens','No app runtime, WCAG conformance, Docker, DB, matching, Mermaid or deployment tests']}
output = vault / '08_Operations/Test_Evidence/DPT-PLAN-012_Planning_Validation.json'
output.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'stock':[{'mode':s['mode'],'exit':s['exit'],'errors':len(s['errors'])} for s in stock],'inherited_findings':len(inherited),'unexplained':unexplained,'scoped_failures':failures,'scoped_result':record['scoped_result'],'markdown_files':markdown_count,'references':len(ids),'route_types':len(route_rows),'diff_check_exit':diff.returncode},ensure_ascii=False))
```
