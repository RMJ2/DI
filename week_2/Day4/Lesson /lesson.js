// // global variable 
// // declared in the global scope 

        // let mood = 'happy'
        // let username = 'Sarah'

// // declraring a function 
// // no parameters because the parentheses are empty:
//             //PARAMETERS   
        // function userInfo (username, age, height) {
        //     console.log('Hello ' + username)
        //     console.log('Age ' + age)
        //     console.log('Height ' + height)
        // }

    // console.log('username ;', username)

// // Invoke or call the function 
// // Argument
        // userInfo('David', 25, 1.7)
        // userInfo('Josh', 27, 1.8)    
        // userInfo('Lior', 31, 1.5)

// // Local means used in the local scope
// // functions, loops, conditionals

// {}




// -------------------------Exercise 1: --------------------------------------------------

// function familyAge (myAge) {
//     // display the age of the mum : twice my age

//     let ageMom = myAge*2;
//     let ageDad = ageMom*1.2; 
//     console.log(`My mum is ${ageMom} years old and my dad is ${ageDad} `);
// }

// familyAge(27); 

// --------------------------------------------------


// let username = 'Lea'

// console.log('1', username) // Lea

// // DECLARING
// function familyAge (myAge) {
//     let username = 'Raoul'
//     console.log('2:', username) // undefined - Lea 
    
//   // in the local scope I can modify a 
//   // variable that was declared in the global scope
//    // changing ......
    
//     username - 'David'
//     console.log('3:', username) // undefined - David
//     // local variables 
//     let ageMum = myAge*2
//     let ageDad = ageMum*1.2
//     console.log(`My mum is ${ageMom} years old and my dad is ${ageDad} `);

//     // INVOKE: 
//     familyAge(50);

// }

// ------------------------------------------------------------

// // 1 FUNCTION = 1 ACTION
// ​
// //calculating the age of the dad
// function familyAge(myAge){ //4th step
// 	let ageDad = myAge*2 
// 	return ageDad //5th step
// }
// ​
// //displaying the details about the dad
// function familyDetail(){ //2nd step
// 	//dadDetail = ageDad = 40
// 	let dadDetail = familyAge(20) //3rd step //6th step
// 	console.log(`My dad is ${dadDetail}`)
// }
// ​
// familyDetail() //1r step


// ------------


// //global variable
// // decared in the global scope
// let username = "Lea"
// ​
// console.log("1:", username) // display Lea
// ​
// //DECLARING
// function familyAge (myAge) {
// 	console.log("2:",username) // display Lea
// 	// In the local scope I can modify a
// 	// variable that was declared in the global scope
// 	// and I can change the global variable
// 	username = "David"
// 	console.log("3:",username) // display David
// 	//local variables
// 	let ageMum = myAge*2
// 	let ageDad = ageMum*1.2
// 	console.log(`The age of my mum is ${ageMum}, the age of my dad is ${ageDad}`)
// }
// ​
// //INVOKE
// familyAge(60)
// ​
// console.log("4:",username) // display David
// ​
// ​
// ​
// //global scope
// console.log(ageMum) // undefined
// ​
// // // LOCAL VARIABLE: IS A VARIABLE DECLARED IN THE LOCAL SCOPE
// // // YOU CANNOT ACCESS A LOCAL VARIABLE IN THE GLOBAL SCOPE

// -----------------------


// // declaring a function
// 				// PARAMETERS
//                 function userInfo (username,age,height) {
//                     console.log("Hello " + username)
//                     console.log("Age " + age)
//                     console.log("Height " + height)
//                 }
//                 ​
//                 //global scope
//                 console.log("username :", username)
//                 ​
//                 // Local means used in the local scope : in a block
//                 // functions, loops, conditionals
//                 ​
//                 // Global means used in the global scope
//                 // outside of a local
//                 ​
//                 ​
//                 // invoke/call the function
//                 // ARGUMENT
//                 userInfo("David",25, 1.7)