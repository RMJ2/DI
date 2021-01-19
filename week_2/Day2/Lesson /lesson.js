


// //  OBJECTS : access the element by the property 
// let users = {
//     username : 'John',
//     password : '1234',
//     email : 'john@gmail.com',
//     logIn : true, 
//     countries : ['israel', 'usa'],
//     friends : {
//         names : ['David', 'Sarah']
//     }
// }


// // 1. display the friends nested object.
// console.log('friends nested object :', user['friends']);

// // 2. display the list of names of his friends. 
// console.log('list of names of his friends :', user['friends']['names']);

// // 3. display the name of best friends : David 
// console.log('name of best friend :', user['friends']['names'][0]);

// ------------------------------------------------------

// // John lives in the USA                            ARRAY
// let sentence = user['username'] + ' lives in the' + user['countries'] [1]
// console.log(sentence);


// //              nameOfObject ['nameOfProperty']
// let firstUser = user['username']
// let emailUser = user['email']

// -------------------------------------------------------

// // ARRAY OF OBJECTS (user = parent, [below are 3 children])
// let users = [
//     {
//         username : 'John',
//         password : 1234
//     },

//     {
//         username : 'Lea',
//         password : 5555
//     },

//     {
//         username : 'David',
//         password : 6767
//     },

// ];

// console.log(users)
// // 1. display the information of the 2nd user (object)
// console.log('2nd user', users[1])

// // 2. display the password of the 2nd user
// console.log('2nd user password', users[1] ['password'])


// CONDITIONALS ----------------------------------------

// if (condition) {
//     // statement
// }

// if (I had money) {
//     I would buy a car
// }



// let bankamount = 1000;
// let accountNumber = 1234;
// if (bankamount >= 500 && accountNumber == 1234 ){
//     // if the condition is true
//     console.log ('I can buy a computer')
// };


// let username == "David"

// if (username == "Lea"){
//     // will run only if the condition is true
//     console.log("Congratulations")
// } else {
//     // will run only if the condition is false.
//     console.log("You are not Lea")
// };




// // number
// let age = 18
// // boolean
// let birthday = true

// if (age == 18 && birthday){
//     // run if the 2 conditions are true
//     ++age
//     console.log ("age", age)
// } else {
//     console.log("You are stil 18")
// }




// //Exercise 1 ----------------------------------------

// let person = 36;
// if (person < 18) {
//   console.log(‘Sorry, you are too young to drive this car. Powering off’);
// } else if (person == 18) {
//   console.log(‘Congratulations on your first year of driving. Enjoy the ride!’);
// } else {
//   console.log(‘Powering On. Enjoy the ride!’);
// }



// SWITCH CASE ----------------------------------------
// let fruit = 'Papayas';

// switch (fruit) {
//   case 'Oranges':
//     console.log('Oranges are $0.59 a pound.');
//     break;
//   case 'Mangoes':
//   case 'Papayas':
//     console.log('Mangoes and papayas are $2.79 a pound.');
//     // expected output: "Mangoes and papayas are $2.79 a pound."
//     break;
//   default:
//     console.log('Sorry, we are out of ' + fruit + 'Oranges');
// }

// Exercise 2 ----------------------------------------

// let a = 2 + 2;
// // a=4 

// switch (a) {
//   case 3:
//     //   If a === 3, respond with "Too small"
//     alert( 'Too small' );
//     break;

//   case 4:
//     // If a === 4, Respond with "exactly"
//     alert( 'Exactly!' );
//     break;

//   case 5:
//       // If a === 5, Respond with "Too Large"
//     alert( 'Too large' );
//     break;

//   default:
//     alert( "I don't know such values" );
// }



// // Exercise 3 ----------------------------------------

// let a = 2 + 2;                                      // a = 4

// switch (a) {                                        // ?
//   case 4:                                           // true
//     alert('Right!');                                // alert
//     break;                                          // break
                                                    
    
//     // Beow will not run, no case available. 
//   case 3: // (*) grouped two cases
//   case 5:
//     //   a===3, Respond with 2 x Alerts below.
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
//     break;

//   default:
//     alert('The result is strange. Really.');
// }
