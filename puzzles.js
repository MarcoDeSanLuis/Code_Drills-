// find common characters in 2 words

const findCommonChars = (word1, word2) => {
  const commonChars = [];
  const charArr1 = word1.toLowerCase().split('');
  word2
    .toLowerCase()
    .split('')
    .forEach(c => charArr1.includes(c) && !commonChars.includes(c)
      && commonChars.push(c));

  console.log(`Common characters: ${commonChars.join(", ")}`);
}

findCommonChars("apple", "pear");