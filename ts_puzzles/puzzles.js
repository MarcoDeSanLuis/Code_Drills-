// find common characters ----------------
function findCommonChars(word1, word2) {
    var charArr1 = word1.toLowerCase().split('');
    var commonChars = [];
    word2.toLowerCase().split('').forEach(function (c) {
        charArr1.indexOf(c) !== -1 && commonChars.indexOf(c) === -1
            && commonChars.push(c);
    });
    console.log("Common characters: ".concat(commonChars.join(", ")));
}
findCommonChars('apple', 'pear');
