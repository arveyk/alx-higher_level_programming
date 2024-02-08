#!/usr/bin/node

const esrever = function (list){
  let list_rev = [];
  for (let len = list.length - 1; len >= 0; len--) {
    list_rev.push(list[len]) 
  }
  return (list_rev);
}
module.exports = esrever;
