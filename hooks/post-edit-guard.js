#!/usr/bin/env node
// MIDU Vibecoder Kit — PostToolUse hook (Edit|Write).
// Silent no-op outside a MIDU project or on non-UI files. Inside one,
// re-checks the two brand regressions this kit has actually hit before:
// Google Fonts Rubik (no Vietnamese subset) and outline:none with no
// :focus-visible replacement (WCAG 2.4.7).

const fs = require('fs');
const path = require('path');
const { isMiduProject } = require('./detect-midu');

let event;
try {
  event = JSON.parse(fs.readFileSync(0, 'utf8'));
} catch (e) {
  process.exit(0);
}

const filePath = event.tool_input && event.tool_input.file_path;
if (!filePath || !/\.(html|css|tsx|jsx)$/i.test(filePath)) process.exit(0);

const cwd = event.cwd || process.cwd();
if (!isMiduProject(cwd)) process.exit(0);

let content;
try {
  content = fs.readFileSync(filePath, 'utf8');
} catch (e) {
  process.exit(0);
}

const warnings = [];
if (/fonts\.googleapis\.com[^"']*Rubik/i.test(content)) {
  warnings.push(
    'Google Fonts Rubik has no Vietnamese subset — use the bundled FZ Rubik ' +
    '("Fz Rubik", design-system/fonts/FzRubik/) instead.'
  );
}
if (/outline\s*:\s*(none|0)\b/i.test(content) && !/:focus-visible/i.test(content)) {
  warnings.push(
    'outline suppressed with no :focus-visible replacement — WCAG 2.4.7 failure. ' +
    'Add a focus ring (see DESIGN.md focus tokens).'
  );
}
if (!warnings.length) process.exit(0);

process.stdout.write(JSON.stringify({
  hookSpecificOutput: {
    hookEventName: 'PostToolUse',
    additionalContext: 'MIDU brand-review guard on ' + path.basename(filePath) + ': ' + warnings.join(' '),
  },
}));
