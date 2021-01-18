// Daily Challenge : Not Bad

// 1.   Create a string that has the word “not” and “bad” inside
// 2.   Create another variable that should find the first appearance of the substring “not” and “bad”.
// 3.   If the ‘bad’ follows the “not”, then it should replace the whole “not”…”bad” substring with ‘good’ than console.log the result.
// 4.   If it doesn’t find “not” and “bad” in the right sequence (or at all), just console.log the original sentence.


// 1.   Create a string that has the word “not” and “bad” inside

let string = 'this dinner is not that bad';
console.log(string);

// 2.   Create another variable that should find the first appearance of the substring “not” and “bad”.

function notBad(sentance) {
    let notindex = sentence.indexOf ('not');
    let badIndex = sentence.indexOf('bad');
    if (notIndex == -1|| badIndex ==-1|| badIndex <notIndex) return sentance;
    return sentence.slice(0, notIndex) + 'good' +sentence.slice(badIndex +3);
}
