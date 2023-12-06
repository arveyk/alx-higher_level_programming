#!/usr/bin/node
const len = process.argv.length;

if (len <= 2) {
  console.log('No argument');
}
if (len == 3) {
  console.log('Argument found');
}
if (len > 3) {
  console.log('Arguments found');
}
