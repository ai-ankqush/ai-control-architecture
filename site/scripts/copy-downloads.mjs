#!/usr/bin/env node
/**
 * postbuild: copy static download assets directly into Retype's output (.retype),
 * which Vercel serves verbatim. Retype does not reliably copy arbitrary non-page
 * files from the input tree, so we place them in the output ourselves.
 *   repo/resources/*.pdf  -> .retype/downloads/*   (served at /downloads/*)
 *   site/static/*         -> .retype/static/*      (served at /static/*, e.g. favicon)
 */
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, "..", "..");           // repository root
const OUT = path.resolve(__dirname, "..", ".retype");       // retype output (site/.retype)

// Not yet published (kept in the repo, but not served): the training course is
// still being finalised, so the Training page shows a "coming soon" placeholder.
const EXCLUDE = new Set(["ACA-Practitioner-Training.pdf"]);

async function copyDir(srcAbs, destRel) {
  let files;
  try { files = await fs.readdir(srcAbs); } catch { return 0; }
  const destAbs = path.join(OUT, destRel);
  await fs.mkdir(destAbs, { recursive: true });
  let n = 0;
  for (const f of files) {
    if (EXCLUDE.has(f)) continue;
    const s = path.join(srcAbs, f);
    const st = await fs.stat(s);
    if (st.isFile()) { await fs.copyFile(s, path.join(destAbs, f)); n++; }
  }
  return n;
}

const dl = await copyDir(path.join(REPO, "resources"), "downloads");
const st = await copyDir(path.join(__dirname, "..", "static"), "static");
console.log(`postbuild: copied ${dl} download(s) -> /downloads and ${st} static file(s) -> /static`);
