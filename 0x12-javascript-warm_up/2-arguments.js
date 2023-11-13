#!/usr/bin/node
let count = 0;
const { argv } = require('node:process');
argv.forEach((val, index) => {
  count = index;
});
if (count <= 1) {
  console.log('No argument');
} else if (count === 2) {
  console.log('Argument found');
} else if (count > 2) {
  console.log('Arguments found');
}
