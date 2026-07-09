// Shared MIDU-project detector for the kit's hooks.
// True if the project carries ANY marker the install paths actually drop in:
//   - DESIGN.md mentioning MenaQ7 (README Option 3), OR
//   - tokens.css / midu-theme.css defining a --midu- custom property
//     (plugin install + README Options 1-2 copy those, NOT DESIGN.md).
// Markers are MIDU-specific (--midu- / MenaQ7) to avoid firing in unrelated projects.
const fs = require('fs');
const path = require('path');

function readSafe(p) {
  try {
    return fs.readFileSync(p, 'utf8');
  } catch (e) {
    return null;
  }
}

function isMiduProject(cwd) {
  const design = readSafe(path.join(cwd, 'DESIGN.md'));
  if (design && /MenaQ7/.test(design)) return true;
  const cssCandidates = [
    'tokens.css',
    'midu-theme.css',
    path.join('design-system', 'tokens.css'),
    path.join('src', 'styles', 'tokens.css'),
  ];
  for (const rel of cssCandidates) {
    const css = readSafe(path.join(cwd, rel));
    if (css && /--midu-/.test(css)) return true;
  }
  return false;
}

module.exports = { isMiduProject };
