#!/usr/bin/node

const { list } = require("./100-data.js");
console.log(list);
console.log(list.map((e, i) => e * i));
