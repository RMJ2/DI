
// EXERCISE 1 ---------------------------------------------------

//  Create 2 variables, x and y. Each of them has a different numeric value.
//  1. Write an if/else statement that checks the biggest number.
//  2. If x equals 5 and y equals 2, the program should display:
//   x is the biggest number

// let x = 5;
// let y = 2;

// if (x > y) {
//     console.log('the number x is the biggest number')
// } else {
//     console.log('the number y is the biggest number')
// }



// EXERCISE 2 -CHIHUAHUA ----------------------------------------

// 1. Create a variable newDog that is equal to the string “Chihuahua”.
// 2. Check and display how many letters are in newDog.
// 3. Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just use 2 console.log).
// 4. Check if the variable newDog equals to “Chihuahua”
//      1. if it does,  display ‘I love Chihuahua, it’s my favorite dog breed’
//      2. else, console.log ‘I dont care, I prefer cats’

// // // 1.
// let newDog = 'Chihuahua';
// // 2. 
//     console.log(newDog.length)
// // 3.
// console.log(newDog.toUpperCase());
// console.log(newDog.toLowerCase());

// // 4. 
// if (newDog == 'Chihuahua') {
//     console.log('I love Chihuahua, its my favourite dog breed')
// } else{
//     console.log('I dont care, I prefer cats')
// }



// // EXERCISE 3 EVEN OR NOT EVEN: ---------------------------------------------------

// // 1.   Ask a number to the user, and save it to a variable.
// // 2.   Check if the variable is an even number
// //         1. If it is, display: “x is an even number’. Where x is the actual number of the user.
// //         2. If it isn’t, display “x is not an even number’. Where x is the actual number of the user

// // 1. take input from the user 
// let number = prompt('Write a number');

// // check if the number is even 
// if (number %2==0){
//     console.log('The number is even');
// }

// // if the number is odd
// else{
//     console.log('The number is odd')
// }





// // EXERCISE 4 - GROUP CHAT: ---------------------------------------------------

// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

// 1. Using the array above, console.log the number of users in a group conversation based on the following rules:
//      If there is no one, display “no one is online”.
//      If there is 1 person, display “<name_user> is online”.
//      If there are 2 people, display “<name_user1> and <name_user2> are online”.
//      If there are n>2 people, display the first two names and add “and n-2 more are online”.
// For example, if there are 5 users, it should display:
// name_user1, name_user2 and 3 more are online


// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
//     let numberOfUsers= users.length;                   //change users.length to new Variable (numberOfUsers)
//     let numberOfPeopleRemaining = numberOfUsers-2;     // New variable = numberOfUsers minus 2 (numberOfPeopleRemaining)

//     if (users.length == 0){                           //if users array is empty / = no one online
//         console.log("no one is online");

//     } else if  (users.length == 1){                    //if users array is 1 users (users[0] + 'is online')
//         console.log(users[0] + 'is online');
    
//     } else if (users.length == 2){                      //if users array is 2 users (users[0] + ' ' + users[1] + 'is online')
//         console.log(users[0] + ' ' + users[1] + 'are online')
//     }
//     else if (users.length >2){                           //if users array is n>2 users (NOPR=numberOfUsers-2)
//         console.log(users[0] + users[1] + 'and' + numberOfPeopleRemaining + 'more are online')
//     }



// -------------------------------------------------------------------------------------


