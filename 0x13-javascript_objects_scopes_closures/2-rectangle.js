#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h) {
      let obj = {};
    }
    else if ((w === 0 || h === 0) || (w < 0 || h < 0)) {
      let obj = {};
    }
    else {
      this.width = w;
      this.height = h;
    } 
  }
}

module.exports = Rectangle;
