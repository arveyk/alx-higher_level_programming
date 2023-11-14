#!/usr/bin/node
let count = 0;
let num;
let num1;
const { argv } = require('node:process');


argv.forEach((val, index) => {
  count = index;
  if (index == 2) {
    num = Number(val);
  }
  if (index == 3) {
    num1 = Number(val);
  }
});


if (count !== 3) {
  console.log('Missing number of occurences');
} else {
  function add (num, num1) {
    return num1 + num;
};
  console.log(add(num + num1));
}

