#!/usr/bin/env node
// MIDU Vibecoder Kit — SessionStart hook.
// Silent no-op outside a MIDU project. Inside one, reminds Claude of the
// brand non-negotiables so they apply even when the prompt doesn't say
// "MIDU" (skill auto-invoke is keyword-triggered; this isn't).

const fs = require('fs');
const path = require('path');

let cwd = process.cwd();
try {
  const input = JSON.parse(fs.readFileSync(0, 'utf8'));
  if (input.cwd) cwd = input.cwd;
} catch (e) {
  // no stdin JSON — fall back to process.cwd()
}

let design;
try {
  design = fs.readFileSync(path.join(cwd, 'DESIGN.md'), 'utf8');
} catch (e) {
  process.exit(0);
}
if (!/MenaQ7/.test(design)) process.exit(0);

const context = [
  'MIDU Vibecoder Kit active (DESIGN.md found in this project).',
  'Non-negotiables: closed palette only (indigo #384B98, magenta #C1368D, sun #EFCA3D + documented neutrals);',
  'FZ Rubik font — never substitute Google Fonts Rubik (no Vietnamese diacritics);',
  'max one gradient CTA per viewport; every interactive element needs a :focus-visible ring (WCAG 2.4.7).',
  'Skills: midu-design-system (build), midu-brand-review (audit), nextjs-frontend, typescript-backend.',
].join(' ');

process.stdout.write(JSON.stringify({
  hookSpecificOutput: {
    hookEventName: 'SessionStart',
    additionalContext: context,
  },
}));
