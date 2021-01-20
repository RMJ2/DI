//      1.Ask a user for several words (separated by commas).
//      2. Push the words into an array.
//      3. Console.log them, one per line, in a rectangular frame.
//      For example, if the user gives you:
//      Hello, World, in, a, frame
//      you will transform it to : ["Hello", "World", "in", "a", "frame"]
//      that will get displayed as   

// Use functions, string methods, array methods and loops

// Hint:

// The number of stars that wraps the sentence, must depend on the length of the longest word.
// Requirements:

// To do this challenge you only need Javascript(No HTML and no CSS)

// 1. & 2. &  3. 

// function wordFrameBuilder (sentance){

// let user = prompt('Tell me something');
// let words = user.split(' ');

// let word = ''; 
// let longest = '';
// for (word of words) {
//     if (word.length > longest.length){
//         longest = word;
//     }
// }

// let length = longest.length; 

// let stars = '';

// for (let i = 0; i < length; i++){
//     stars = stars.concat('*')
// }
// console.log(stars);

// let topAndBottom ='**' + (stars) + '**';


// // console.log(longest);

// console.log(topAndBottom);

// for (word of words) {

//     let spaceLength = length - word.length;
//     let space = '';
//     for(let x = 0; x < spaceLength; x++){
//         space = space.concat(' ')
//     } 

//     console.log('* '+  word + ' *');
// }

// console.log(topAndBottom);



//------------

function wordFrameBuilder(sentence) {
    // let sentence = 'hello world in a frame';
    let sentenceArray = sentence.split(' ')
    // console.log(sentenceArray);
    let word = '';
    let longest = '';
    for  (word of sentenceArray) {
        if (word.length > longest.length) {
            longest = word;
        }
    }
    let length = longest.length;
    let stars = ''
    for (let i = 0;i < length; i++) {
        stars = stars.concat('*')
    }
    // console.log(stars);
    let topAndBottom = '**' + stars +  '**';
    // console.log(longest);
    console.log(topAndBottom);
    for (word of sentenceArray) {
        let spaceLength = length - word.length;
        let space = '';
        for (let x = 0; x < spaceLength; x++) {
            space = space.concat(' ')
        }
        console.log('* ' + word + space + ' *');
    }
    console.log(topAndBottom);
}
wordFrameBuilder(prompt('please enter a sentence'))












