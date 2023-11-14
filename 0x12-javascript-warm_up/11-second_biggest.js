#!/usr/bin/node
/*const { argv } = require('node:process'); */
let count = 0;
let num = 0;
let num2 = 0;
/*
argv.forEach((val, index) => {
  count = index;
  if (count === 2) {
    console.log(`${val}`);
  }
});
*/
if (count == 1) {
  console.log('0');
} else while (count >= 2 ) {
  if (Number(process.argv[count]) > num) {
    num2 = num;
    num = Number(process.argv[count]);
  }
  count -= 1;
}
console.log(num2);
