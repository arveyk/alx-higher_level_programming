#!/usr/bin/node
const { argv } = require('node:process');
let var1;
argv.forEach((val, index) => {
  count = index;
  if (count === 2) {
    var1 = val;
  }
});
let num = Number(var1);
if ((typeof num) === Number) {
  console.log('My number is: ', var1);
} else {
  console.log('Not a number');
}
