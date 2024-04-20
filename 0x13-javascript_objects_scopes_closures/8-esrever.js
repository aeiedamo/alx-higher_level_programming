#!/usr/bin/node

const esrever = (list) => list.map((e, i) => list[list.length - 1 - i]);

module.exports = { esrever };
