#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  print2 (p) {
    let printChar = '';
    for (let span = 0; span < this.width; span++) {
      printChar += p;
    }
    for (let depth = 0; depth < this.height; depth++) {
      console.log(printChar);
    }
  }

  charPrint (c) {
    if (c) {
      this.print2(c);
    } else {
      this.print();
    }
  }
}
module.exports = Square;
