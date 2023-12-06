#!/usr/bin/node
const len = process.argv.length;

if (len <= 1) {
  console.log('No argument');
} else if (len === 2) {
  console.log('Argument found');
} else if (len > 2) {
  console.log('Arguments found');
}
