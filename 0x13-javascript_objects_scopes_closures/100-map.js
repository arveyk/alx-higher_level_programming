#!/usr/bin/node
const oldList = require('./100-data').list;
const newList = oldList.map((x, index) => x * index);
console.log(oldList);
console.log(newList);
