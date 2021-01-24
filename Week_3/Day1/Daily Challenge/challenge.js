// 1. Create an array of planets of the solar system
let planets =['Earth', 'Jupiter', 'Mercury', 'Venus', 'Mars', 'Saturn', 'Uranus', 'Neptune'];
// console.log(planets);
let colors =['red','blue','green','yellow','purple','white','brown','orange','pink'];

let moons=[1, 79, 0, 0, 2, 62, 27, 14];

// 2. For each planet, in the array, create a div using createElement. This div should have a class named ‘planet’.
for (i=0; i<planets.length; i++) {
    let newDiv = document.createElement('div');
    // newDiv.className = 'planet';
    newDiv.classList.add(planets[i], 'planet');
// 3. Each planet should have a different background color. (Hint: add a new class to each planet)
newDiv.style.backgroundColor=colors[i]
    newDiv.style.margin='30px'
 // 4. Finally append each div to the body.  
    let name=document.createTextNode(planets[i],'planets')
    newDiv.appendChild(name)
    document.body.appendChild(newDiv)
    console.log(newDiv);  

    // 5. Bonus Do the same process for moons. Be careful, each planet has a certain amount of moons; How should you display them ? 

    let ml=120 
    if (moons[i]!=0) {
       for (let h=0; h<moons[i]; h++){
           ml+=50;
           let divMoon=document.createElement('div'); 
           divMoon.classList.add('moon');
           divMoon.style.marginLeft=ml + 'px';
            newDiv.appendChild(divMoon);
       }
        
    }

}

