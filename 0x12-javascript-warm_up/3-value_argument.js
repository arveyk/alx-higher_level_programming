#!/usr/bin/node
const { argv } = require('node:process');
let count = 0
argv.forEach((val, index) => {
  count = index;
  if (count === 2) {
    console.log(`${val}`);
  }
});
if (count < 2) {
    console.log('No argument');
} 
