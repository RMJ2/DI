// 1. Give to all paragraphs inside the <article> tag the class of para_article.
// 2. Remove the last paragraph in the article.
// 3. Add an event listener so that when you click on the h2, it is removed from the DOM.
// 4. Set the font size of the h1 to be a random pixel size from 0 to 100.
// 5. Hide the 1st paragraph, when it’s clicked. (use the display property )
// 6. Get the values from the inputs and append them to the end of the html, inside a table.
// 7. Bonus: Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.

// let className = document.getElementsByTagName('p');
// className.className += ' para_article'; 
// element.classList.add('para_article');

let x = document.getElementsByTagName("p")
x.className = 'para_art'
console.log(x.className)

let y = document.getElementsByTagName('p')[3];
y.remove();

let h2 = document.getElementsByTagName('article')[0].getElementsByTagName('h2')[0]
h2.addEventListener("click", function() {
    let z = document.getElementsByTagName('article')[0].getElementsByTagName('h2');
    z[0].remove();
});

let randomNumber = Math.random()*100
console.log(randomNumber)
let size = `${randomNumber}px`
let h1 = document.getElementsByTagName('article')[0].getElementsByTagName('h1')[0]
h1.style.fontSize = size

let p = document.getElementsByTagName('p')[0];

p.addEventListener("click", function() {
    let p = document.getElementsByTagName('p')[0];
    p.style.display = "none"
});


