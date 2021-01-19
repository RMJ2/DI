// Remove the Banana from the array.
// Sort the array in order.
// Put “Kiwi” at the end of the array.
// Remove “Apples” from the array. Don’t use the same method as in the question 1.
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
// You should have at the end:
// ["Kiwi", "Oranges", "Blueberries"]


let fruits = ['Banana', 'Apples', 'Oranges', 'Blueberries']
fruits.shift();
console.log(fruits)
fruits.sort()
console.log(fruits)
fruits.push('Kiwi')
console.log(fruits)
fruits.splice(0, 1)
console.log(fruits)
fruits.reverse()
console.log(fruits)

// Using this array :

// let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// Access the item “Oranges”.

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits [1] [1] [0]);


