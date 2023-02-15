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

// find most common characters in a sentence

const findMostCommonChars = (sent) => {
  const charMap = {};
  const mostCommonChars = [];
  let maxFreq = 0;

  sent.toLowerCase().split('').forEach(c => {
    charMap[c] ? charMap[c]++ : charMap[c] = 1;
  })

  for (c in charMap) charMap[c] > maxFreq && (maxFreq = charMap[c]);
  for (c in charMap) charMap[c] == maxFreq && mostCommonChars.push(c);

  console.log(`Most common characters: ${mostCommonChars.join(", ")} | Occurences: ${maxFreq}`);
}

findMostCommonChars("Yabba, dabba, doo!!");