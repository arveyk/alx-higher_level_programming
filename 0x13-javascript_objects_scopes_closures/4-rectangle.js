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

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = Rectangle;
