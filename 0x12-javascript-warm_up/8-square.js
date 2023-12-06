#!/usr/bin/node
let num  = parseInt(process.argv[2]);
let hash = 'X';

if (!num) {
  console.log('Missing number of occurences');
} else {
  let count = num
  while (count > 1) {
    hash += "X";
    count -= 1;
  }
  for (let num2 = num; num2 > 0; num2--) {
    console.log(hash);
  }
}

