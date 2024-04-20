#!/usr/bin/node

const nbOccurences = (list, searchElement) =>
  list.filter((x) => x === searchElement).length;

module.exports = { nbOccurences };
