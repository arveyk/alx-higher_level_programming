#!/usr/bin/node
let count = 0;
let num;
let hash = '#';
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
  while (num > 1) {
    for (let num2 = num; num2 > 0; num2--) {
	    console.log(hash * num2);
    }
    num -= 1;
  }
}

