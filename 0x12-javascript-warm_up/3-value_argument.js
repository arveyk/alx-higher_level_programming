#!/usr/bin/node
const { argv } = require('node:process');
argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
});
