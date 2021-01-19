// //    1. Guess the answers
   
//     5 + "34"            =   534
//     5 - "4"             =   1
//     10 % 5              =   0
//     5 % 10              =   5
//     "Java" + "Script"   =   "JavaScipt"
//     " " + " "           =   ""
//     " " + 0             =   "0"
//     true + true         =   2
//     true + false        =   1
//     false + true        =   1
//     false - true        =   -1
//     3 - 4               =   -1
//     "Bob" - "bill"      =   NaN 



    // 2. Favourite colour - Write a simple JavaScript program to join all elements of the following array into a string.

                //     let me = ["my","favorite","color","is","blue"]

                // // Answer: 
                // let meString = me.join(' '); 
                // console.log(meString)


// // 3. Mix Up
// // 1. Create two strings
// // 2. Create a variable which value is the concatenation of the two strings (separated by a space) slicing out and swapping the first 2 characters of each.

// // Example :
// // let str1 = 'mix', let str2 = 'pod' 
// // let newWord should be equal to 'pox mid'



// // Answer #3
// // substring = cannot seem to figure it out!

// // let str = "pod mix";
// // let newStr = str.replace(/(po|mi)/g, function(x) {
// //     return x === "po" ? "mi" : "po";});

// or

        // console.log('Exercise 3:')
        // let string1 ='pod';
        // let string2 ='mix';

        // let string44= string1.substring(0,string1.length-1) +string2.substring(string2.length-1)
        // console.log(string44)

        // let string45= string2.substring(0,string2.length-1) +string1.substring(string1.length-1)
        // console.log(string45)
        // console.log(string44 + ' ' + string45)






let userGrade = parseInt(prompt('What is your grade?'))

console.log(typeof(userGrade));
console.log(userGrade)


