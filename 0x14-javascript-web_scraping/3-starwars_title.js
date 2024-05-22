#!/usr/bin/node
// a script that prints the title of a Star Wars movie where the
// episode number matches a given integer.

const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
