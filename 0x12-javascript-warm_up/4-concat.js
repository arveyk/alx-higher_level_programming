#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
let var1;
let var2;
argv.forEach((val, index) => {
  count = index;
  if (count === 2) {
    var1 = val;
  }
  if (count === 3) {
    var2 = val;
  }
});

console.log(var1 + ' is ' + var2);