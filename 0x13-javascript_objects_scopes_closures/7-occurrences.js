#!/usr/bin/node

const nbOccurences = function (list, searchElement) {
  let lVar = 0;
  let count = 0;
  while (lVar < list.length) {
    if (list[lVar] === searchElement) {
      count++;
    }
    lVar++;
  }
  return (count);
};

module.exports.nbOccurences = nbOccurences;
