#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h) {
      const obj = Rectangle.class;
      return obj;
    } else if ((w === 0 || h === 0) || (w < 0 || h < 0)) {
      const obj = Rectangle.class;
      return obj;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
