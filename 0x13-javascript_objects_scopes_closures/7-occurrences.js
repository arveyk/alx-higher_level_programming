#!/usr/bin/node

nbOccurences = function (list, searchElement) {
  let l_var = 0;
  let count = 0;
  while (l_var < list.length) {
    if (list[l_var] == searchElement) {
      count++; 
    }
    l_var++;
  }
  return (count);
}

module.exports.nbOccurences = nbOccurences
