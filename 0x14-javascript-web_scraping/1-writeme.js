#!/usr/bin/node
// a script that writes a string to a file.

const FS = require('fs');
FS.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) console.log(err);
});
