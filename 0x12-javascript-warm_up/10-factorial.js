#!/usr/bin/node
const num = parseInt(process.argv[2]);

let number = num;

if (isNaN(num)) {
  console.log(1);
} else {
  function fact(first) {
    if (first == 1) {
      return (1);
    }
    return (first * fact(first - 1));
  }
  console.log(fact(number));
}
