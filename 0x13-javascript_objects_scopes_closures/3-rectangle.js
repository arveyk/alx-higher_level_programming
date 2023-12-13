#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h) {
      return Rectangle.class;
    } else if ((w === 0 || h === 0) || (w < 0 || h < 0)) {
      return Rectangle.class;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let printChar = '';
    for (let span = 0; span < this.width; span++) {
      printChar += 'X';
    }
    for (let depth = 0; depth < this.height; depth++) {
      console.log(printChar);
    }
  }
}

module.exports = Rectangle;
