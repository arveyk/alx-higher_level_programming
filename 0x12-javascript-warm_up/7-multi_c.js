#!/usr/bin/node
let count = 0;
let num;
const { argv } = require('node:process');

argv.forEach((val, index) => {
  count = index;
  if (index == 2) {
    num = Number(val);
  }
});

if (count == 1) {
  console.log('Missing number of occurences');
} else {
  while (num > 0) {
    console.log('C is fun');
    num -= 1;
  }
}
export * from "7-multi_c"
