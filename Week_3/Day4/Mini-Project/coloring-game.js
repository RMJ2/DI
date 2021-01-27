// mainGrid = create 60x24 rows/columns (1,440 squares)
let colorsave = 'white'
let mouseDown = false
let gridRows = 60
let gridColls = 24
const mainGrid = document.getElementById("mainGrid");
function makeRows(rows, cols) {
    for (let c = 0; c < (rows * cols); c++) {
    let cell = document.createElement("div");
    cell.addEventListener("mousedown", function() {
        mouseDown = true 
    })
    cell.addEventListener("mouseup", function() {
        mouseDown = false
    })
    cell.addEventListener("mouseover", function(event){
     if (mouseDown) {let div = document.getElementById(event.currentTarget.id); div.style.backgroundColor=colorsave; console.log(div.style.backgroundColor) }})
    cell.setAttribute("id", c)
    cell.className = 'grid-item'

    mainGrid.appendChild(cell)
  };
};
makeRows(gridColls, gridRows); // call the function

// funtion paint (){

// }

// sideBar = create 3x8 rows/columns
const sideBar = document.getElementById("sideBar");
function makePallet(rows, cols) {
      for (let c = 0; c < (rows * cols); c++) {
        let cell1 = document.createElement("div");
        cell1.addEventListener('click', choose)     //add attribute
        cell1.className = 'pallet-item'
        sideBar.appendChild(cell1)
      };
    };
    makePallet(3, 8); // call the function


//function to select and save background color in pallet.    
function choose(event){
    console.log(event.target.style.backgroundColor); //selects the color
    colorsave = event.target.style.backgroundColor;
}

// array of colors for the pallet.
(function PalletColors() {
var colors = 
        ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
        '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
        '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A', 
        '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
        '#66994D'],

        divs = Array.from(document.querySelectorAll('.pallet-item'));
    divs.forEach(function(div, index) {
         div.style.backgroundColor = colors[index % colors.length];
     });
  })();

  function clearbtn(){ console.log("clearbtn")
    for (let x = 0; x < gridColls * gridRows ; x++){
        let div = document.getElementById(x)
        div.style.backgroundColor='white'
    }
  }
