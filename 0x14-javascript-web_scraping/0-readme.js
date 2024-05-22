#!/usr/bin/node
// to read from file

const FS = require('fs');
FS.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
