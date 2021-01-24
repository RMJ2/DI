// //How to change the text content of the 3rd li to "John"
// ​
// //get the body
// let bodyWebsite = document.body
// //get the div
// let divWebsite = bodyWebsite.firstElementChild
// 				//bodyWebsite.children[0]
// //get the ul
// let ulWebsite = divWebsite.firstElementChild
// //get the li
// let liThirdWebsite = ulWebsite.lastElementChild
// console.log(liWebsite)
// ​
// //change the text node of the li
// liThirdWebsite.textContent = "John"
// ​
// //get the second li of the ul
// let liSecondWebsite = liThirdWebsite.previousElementSibling
// console.log("Second li : ", liSecondWebsite)
// ​
// //get the parent of the li
// console.log("parent of li: ", liSecondWebsite.parentNode)


//---------------------Exercise 1-------------------------

// //get the body 
// let bodyWebsite = document.body;

// // 1. get the div 1/2
// let divWebsite = bodyWebsite.firstElementChild;
// // 1. get the div 2/2
// let divWebsite = children[0];


// // 2. get the ul 1/2
// let ulWebsite = bodyWebsite.nextElementSibling;
// //2. get the ul 2/2
// let ulWebsite = children[1];


// //3. get the second li(with pete) 1/2
// let liWebsiteTwo = ulWebsite.lastElementChild;
// // 3. get the second li (with pete) 2/2
// let liWebsiteTwo = ulWebsite.children[1];


//------------DOM Attributes----------

let divWebsite = document.getElementById('usersTitle');
console.log('div: ', divWebsite);

// let listWebsite = document.getElementsByClassName('username');
// console.log('list: ', listWebsite[0])


let bodyWebsite = document.body
//create the div element
let newDiv = document.createElement('div');
// newDiiv.setAttribute('class', 'newDiv'); //how to change the classes
// newDiv.classList.add('newdiv', 'olddiv') //how to change the classes
// newDiv.classList.toggle('newdiv', true)


for (let i = 0; i < 5; i++){    //we can use a loop to create multiple paragraphs together (instead of below this loop)
    let newParagraph = document.createElement('p');
    newParagraph.classname = 'welcomeUser + i';
    let newContent = document.createTextNode('Hello new users' + i );
    newParagraph.appendChild(newContent);
    newDiv.appendChild(newParagraph);
}   
bodyWebsite.appendChild(newDiv);


// // //create the p element
// // let newParagraph = document.createElement('p');
// // //create the content (text node)
// // let newContent = document.createTextNode('Hello new users');

// // //add the content to the paragraph (appendChild is appending to the parent)
// // newParagraph.appendChild(newContent)

// // //add the paragraph to the div 
// // newDiv.appendChild(newParagraph)

// //add the div to the body 
// bodyWebsite.appendChild(newDiv)

