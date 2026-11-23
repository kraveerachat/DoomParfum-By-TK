/**
 * Scans a built output directory (for example the runtime image's /app, copied out) for boundary
 * violations. Usage: node scripts/scan-output.ts <directory>
 */
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join, relative } from "node:path";

const root = process.argv[2];
if (!root) {
  console.error("Usage: node scripts/scan-output.ts <directory>");
  process.exit(2);
}

const all = readdirSync(root, { recursive: true, withFileTypes: true })
  .filter((f) => f.isFile())
  .map((f) => join(f.parentPath, f.name));
const name = (file: string) => relative(root, file).replaceAll("\\", "/");
const problems: string[] = [];

const badPath = /(^|\/)(\.env(\..*)?|.*\.(pem|key|dump|sqlite|sql|py|map)|\.git|.*database\/.*|matching_math\/.*|Structure DB.*)$/i;
for (const file of all) {
  const path = name(file);
  if (path.startsWith("node_modules/")) continue;
  if (badPath.test(path)) problems.push(`forbidden file: ${path}`);
}

const secret = /-----BEGIN [A-Z ]*PRIVATE KEY|\bgh[pousr]_[A-Za-z0-9]{30,}|\bAKIA[0-9A-Z]{16}\b|postgres(?:ql)?:\/\/|\bsk-[A-Za-z0-9]{30,}/;
const personal = /[A-Za-z]:[\\/]+Users[\\/]/;
const fixture = /mock-perfume-0\d\d|paper-study-[a-l]|Luthmere|DoomParfum mock atelier/;
let scanned = 0;
for (const file of all) {
  const path = name(file);
  if (path.startsWith("node_modules/") || statSync(file).size > 8_000_000) continue;
  const text = readFileSync(file, "latin1");
  scanned += 1;
  if (secret.test(text)) problems.push(`secret-like content: ${path}`);
  if (personal.test(text)) problems.push(`host path: ${path}`);
  if (path.startsWith(".next/static/") && fixture.test(text)) problems.push(`fixture payload in an immutable asset: ${path}`);
  if (path.startsWith(".next/static/") && /fonts\.(googleapis|gstatic)\.com/.test(text)) problems.push(`remote font: ${path}`);
}

console.log(`Scanned ${scanned} of ${all.length} files outside node_modules.`);
if (problems.length) {
  console.error(problems.join("\n"));
  process.exit(1);
}
console.log("No boundary violation found.");
