#!/usr/bin/node
const num = parseInt(process.argv[2]);
const num1 = parseInt(process.argv[3]);

function add (num, num1) {
  return num1 + num;
}
console.log(add(num, num1));
