// A community build has no upstream updater signing key. Keep it on the
// explicitly downloaded version instead of installing upstream packages.
const fs = require('node:fs');
fs.writeFileSync(
  'src/js/auto_update.bundle.js',
  '/* Community macOS build: automatic updates disabled. */\n'
);
