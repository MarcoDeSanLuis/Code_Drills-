// find common characters ----------------

function findCommonChars(word1: string, word2: string) {
  const charArr1: string[] = word1.toLowerCase().split('');
  const commonChars: string[] = [];

  word2.toLowerCase().split('').forEach(c => {
    charArr1.indexOf(c) !== -1 && commonChars.indexOf(c) === -1
      && commonChars.push(c)
  });

  console.log(`Common characters: ${commonChars.join(", ")}`);
}

findCommonChars('apple', 'pear');