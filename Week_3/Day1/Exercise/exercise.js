   //-------------------EXERCISE 1 - Change the navbar---------------
   
   // 1. In the div above, change the value of the identity attribute (id) from navBar to socialNetworkNavigation, using the setAttribute method.
    // 2. We are going to add a new li to the ul.
        // First, create a new li tag (use the createElement method)
        // Then create a new text node with “Logout” as its specified text.
        // Append the text node to the newly created list node (li).
        // Finally, append this updated list node to the unordered list above, using the appendChild method.
    // 3. Bonus
        // Use the firstChild and the lastChild properties to retrieve the first and last li elements under the parent ul node. Display the text of each link.(Hint: nodeValue property).


// // 1.
//         let navBar =  document.getElementById('navBar');
//         console.log(navBar);
//         navBar.setAttribute('id', 'socialNetworkNavigation');

// // 2.
//         let ul = document.getElementsByTagName('ul')[0] // first acces the 'ul'
//         console.log(ul)
     

//         let liNew = document.createElement ('li');  //access LI
//         let anchor = document.createElement('a');   //Access 'a' tag
//         let att = document.createAttribute('href'); //access href 
//         att.value = '#'                             //assigned a value '#' to href
//         anchor.setAttributeNode(att);
//         let text = document.createTextNode('Logout'); // assign text
//         anchor.appendChild(text);       // attach 'text' to 'anchor'
//         liNew.appendChild(anchor);      // attach 'anchor' to 'liNew'
//         ul.appendChild(liNew);          // attach 'liNew' to 'ul'

//         // access ul 
//         console.log(liNew);


// // 3. Bonus
//         let newUl = document.getElementsByTagName("ul")[0].firstElementChild;
//         let newUlLast = document.getElementsByTagName("ul")[0].lastElementChild;


//         // let firstLi = document.getElementById ('liNew').firstChild;
//         // let txt = "";
//         // txt += 'The node name: ' + firstLi.nodeName + '<br>';
//         // txt += 'The node value: ' + firstLi.nodeValue + "<br>";
//         // txt += "The node type: " + firstLi.nodeType;

//         console.log(newUl);
//         console.log(newUlLast);



// --------------------EXERCISE 2 USERS -----------------------------------------

// 1.   Change the name “Pete” by “Richard”
// 2.   Change each first name of the <ul> by your name
// 3.   Add at the end of each <ul>, a <li> that says “Hey students”
// 4.   Delete the <li> Sarah
// 5.   Bonus
//           Add a class “student_list” to both of the <ul>
//           Add the class “university” and “attendance” to the first <ul>

// 1. access ul-1, li-2;

let liTwo = document.getElementsByTagName('li')[1].innerHTML ='Richard'; //select li-2(pete) and change to Richard
console.log(liTwo)

//2. 
let collectionLi = document.getElementsByTagName('li').length;
   //find out how many li we have(5)
//    console.log(collectionLi)

// option 1 - would loop all the names:
//    for (let i=0; i<collectionLi; i++){
//    let liTwo = document.getElementsByTagName('li')[i].innerHTML ='Josh';
//    }
// console.log(collectionLi)

// option 2 - first (li) inside the (ul)

let allUl = document.getElementsByTagName('ul');


for (let selectedUl of allUl ){
    selectedUl.firstElementChild.innerHTML = 'Josh'
    let liNew = document.createElement('li'); //3. created a new 'li'   //='Hey Students'  
    let text = document.createTextNode('Hey Student!') //3. create text
    liNew.appendChild(text); //3. appendChild to liNew
    selectedUl.appendChild(liNew); //3. appendChild to selectedUl
    
}

// 3.  Add at the end of each <ul>, a <li> that says “Hey students” 
        //(see above)



// 4. Delete the <li> Sarah

let liFive = document.getElementsByTagName('li')[4];        //name variable 'Sarah'
let secondUl = document.getElementsByTagName('ul')[1];      //name variable 'ul' two, position 'li' two (sarah).

secondUl.removeChild(liFive);                           //remove item(sarah)
console.log(liFive);                                    //Print check.



//-------------------------------------------------------------