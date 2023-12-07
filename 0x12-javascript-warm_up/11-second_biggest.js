#!/usr/bin/node
let num = parseInt(process.argv[2]);
let num2 = parseInt(process.argv[3]);
const count = process.argv.length;
let trav = 2;

if (!num || !num2) {
  console.log('0');
} else {
  while (trav < count) {
    if ((parseInt(process.argv[trav])) > num) {
      num2 = num;
      num = parseInt(process.argv[trav]);
    }
    trav += 1;
  }
  console.log(num2);
}
