#!/usr/bin/env node
// Riscarica le skill ponytail vendorizzate dall'upstream. Uso: node scripts/update-ponytail.mjs
import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const repo = 'DietrichGebert/ponytail';
const branch = 'main';
const skills = ['ponytail', 'ponytail-review', 'ponytail-audit', 'ponytail-debt', 'ponytail-gain', 'ponytail-help'];
const dest = join(dirname(fileURLToPath(import.meta.url)), '..', '.opencode', 'skills');
const raw = (path) => `https://raw.githubusercontent.com/${repo}/${branch}/${path}`;

async function get(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${url}: HTTP ${res.status}`);
  return res.text();
}

for (const skill of skills) {
  await mkdir(join(dest, skill), { recursive: true });
  await writeFile(join(dest, skill, 'SKILL.md'), await get(raw(`skills/${skill}/SKILL.md`)));
  console.log(`updated ${skill}`);
}

await writeFile(join(dest, 'ponytail', 'LICENSE'), await get(raw('LICENSE')));

const commit = await (await fetch(`https://api.github.com/repos/${repo}/commits/${branch}`)).json();
await writeFile(join(dest, '.ponytail-rev'), `${commit.sha}\n`);
console.log(`ponytail ${commit.sha.slice(0, 7)} (${commit.commit.committer.date})`);
