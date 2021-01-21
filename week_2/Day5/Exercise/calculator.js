// let elm = document.getElementById('calc');
// console.log(elm); 

let calcDisplay = document.getElementById("calcDisplay"); //html source




let arr = [];                    // need an array to store our numbers 
function my_f(sign){            // we make a function
    arr.push(sign);             // to push each sign into an array 
    console.log(arr);           // we make a variable str to join the array into a string! using '' we enable to have double number. (77 instead of 7,7)
    let str = arr.join('');  
    calcDisplay.innerHTML=sign;
}


function calculate(){           // we make a variable str to join the array into a string! using '' we enable to have double number. (77 instead of 7,7)
    let str = arr.join('');     
    console.log(str);
    let calc = eval(str);       // eval takes the string and calculates it.
    console.log(calc)
    calcDisplay.innerHTML=calc;
}

function reset(){               // create a reset button to clear all of the data. 
    arr = []; 
    calcDisplay.innerHTML='';  
}

function backspace(){
    arr.pop();
}




//   if(sign==="="){
//     console.log(arr);
//     let str = arr.join('');
//     console.log(str);
//     let calc = eval(str);
//     console.log(calc);
//   }
//   else if(sign==='reset'){
//     arr = []
//   }
//   else{
//     arr.push(sign)
//   }

// my_f(6);
// my_f(6);
// my_f("+");
// my_f(3);
// my_f("+");
// my_f(10);