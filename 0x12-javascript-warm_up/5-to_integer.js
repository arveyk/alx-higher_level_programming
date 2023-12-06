#!/usr/bin/node
/* const argv = require('node:process'); */
const argv = process.argv[2];

let num = parseInt(argv);
if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number is: ', num);
}
