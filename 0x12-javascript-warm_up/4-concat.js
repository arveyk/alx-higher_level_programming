#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
let var_1;
let var_2;
argv.forEach((val, index) => {
  count = index;
if (count === 2) {
  var_1 = val;
}
if (count === 3) {
  var_2 = val;
}
});

console.log(var_1 + ' is ' + var_2);
