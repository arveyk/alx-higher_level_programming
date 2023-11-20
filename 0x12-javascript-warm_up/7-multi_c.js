#!/usr/bin/node
const argv = parseInt(process.argv[2]);


if (!argv) {
  console.log('Missing number of occurences');
} else {
  for (let m = 0; m < argv; m++) {
    console.log('C is fun');
  }
}
