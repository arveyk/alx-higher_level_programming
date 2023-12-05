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
   
  }
}

module.exports = Rectangle;
