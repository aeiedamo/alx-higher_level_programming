#!/usr/bin/node

let logMeCount = 0;

const logMe = (e) => {
  console.log(`${logMeCount}: ${e}`);
  logMeCount++;
};

module.exports = { logMe };
