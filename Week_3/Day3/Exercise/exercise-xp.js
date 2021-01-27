
// 1, DONE retrieve the div we want to move: animate (getElementById)
// let animate = document.getElementById('animate');


// 2. ALMOST DONE create a function to move the red box. 


// 3. DONE  use the left or right properties - left property because we are pushing from left to right
// css properties
// top: space from the top to the element
// bottom: space form the bottom to the element
// left: space from the left to the element
// right: space from the right to the element

// 4. setInterval: repetition depending on the timer we do the action X every Y millisecond. (-5 ms)

// 5.DONE We create the position of the object that needs to be moved. (postion 0).
// position 0 
// action x of the setInterval function is to increase the position by 1 everytime. 

// 6. We need to stop the interval from running when it reaches the right corner 
        // when we reach 350px we stop 

// 7. how do we start an interval: setInterval: let timerInterval = setInterval (function called, timer: every 5 ms)
// how do we stop an interval   clearInterval: (timerInterval)


let button = document.getElementById('btn')     //create variable for the button 
    button.addEventListener('click', myMove)    // event listener for button click


//global variables - cannot be read inside the functions    
let position;

function myMove () {    // the button will be the only way to move the red box
    position = 0            
    let timerInterval = setInterval(moveRedBox, 5)    //variable for timer (start and milliseconds speed)
}

function moveRedBox (){                                   // function name
    let animateDiv = document.getElementById('animate');  // variable used to locate the div in html  
    if (position ==350){                                  // where to end the Timer interval (starting from 0 above)
        clearInterval(timerInterval)                      // used to stop the moving of the box
    } else {
        position++;                                       // add 1 to the position. 
        animateDiv.style.left = position + 'px';
    } 
}