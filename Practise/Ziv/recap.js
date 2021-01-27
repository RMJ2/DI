
// function 1 - exercise
// function my_func_1(p1,p2){
//     return p1+p2
// }

// let a = my_func_1(2,3);
// console.log(a);


// -------------------- Exercise ------------------------------

// 1. create a function that get a name as parameter 
// 2.check if name exist in the array 
// 3. yes - return exist/the name
// 4. no - return nit exist
// 5. return with at the end @gmail.com

// let names = ['ziv','matan','jakie','benjie']        

// function retname(p) {                               
        
//     // Loop the array (length)
//     for(let i=0; i <names.length; i++) {    
//         //find the name        
//         if (p===names[i]){    
//             //to add the extension (email) and then return the extension.                     
//             let mail = addEmail(names[i]);
//             return mail;
//         }
// }
//     return 'NOT EXIST';
// }

// function addEmail(name){
//     return name +'@gmail.com'   
// }
// let n = retname('matan');
// console.log(n);


// -------------------- second option ------------------------------

let names = ['ziv','matan','jakie','benjie']        

function retname(p) {                               
        
    // Loop the array (length)
    for(let i=0; i <names.length; i++) {    
        //find the name        
        if (p===names[i]){    
            //to add the extension (email) and then return the extension.                     
            let mail = addEmail(names[i]);
            return mail;
        }
}
    return 'NOT EXIST';
}

// function addEmail(name){
//     return name +'@gmail.com'  

const addEmail = function(name){    // this changes
    return name +'@gmail.com'  


}
let n = retname('matan');
console.log(n);

