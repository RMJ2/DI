// 

// let i = 0
// while (i < users.length){
//   console.log(i)
//   i++
// }

const users = [
  {
    id: 1,
    name: 'Leanne Graham',
    username: 'Bret',
    email: 'Sincere@april.biz'
  },
  {
    id: 2,
    name: 'Ervin Howell',
    username: 'Antonette',
    email: 'Shanna@melissa.tv'
  },
  {
    id: 3,
    name: 'Clementine Bauch',
    username: 'Samantha',
    email: 'Nathan@yesenia.net'
  },
  {
    id: 4,
    name: 'Patricia Lebsack',
    username: 'Karianne',
    email: 'Julianne.OConner@kory.org'
  },
  {
    id: 5,
    name: 'Chelsey Dietrich',
    username: 'Kamren',
    email: 'Lucio_Hettinger@annie.ca'
  },
  {
    id: 6,
    name: 'Mrs. Dennis Schulist',
    username: 'Leopoldo_Corkery',
    email: 'Karley_Dach@jasper.info'
  },
  {
    id: 7,
    name: 'Kurtis Weissnat',
    username: 'Elwyn.Skiles',
    email: 'Telly.Hoeger@billy.biz'
  },
  {
    id: 8,
    name: 'Nicholas Runolfsdottir V',
    username: 'Maxime_Nienow',
    email: 'Sherwood@rosamond.me'
  },
  {
    id: 9,
    name: 'Glenna Reichert',
    username: 'Delphine',
    email: 'Chaim_McDermott@dana.io'
  },
  {
    id: 10,
    name: 'Clementina DuBuque',
    username: 'Moriah.Stanton',
    email: 'Rey.Padberg@karina.biz'
  },
  {
    id: 11,
    name: 'Yosi & Isaac DuBuque',
    username: 'Yosi.Isaac',
    email: 'yosi.isaac@karina.biz'
  }
];

// while loops:
function getData(arr){
  let i = 0
  while (i < arr.length){ 
    console.log(arr[i].name + " 555 " + arr[i].username + " 555 " + arr[i].email);
  i++
  }
}
getData(users)

// function and for loops:
// function getData(arr){
//   for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i].name + " " + arr[i].username + " " + arr[i].email);
//   }
//   for(x in arr){
//     console.log(arr[x].name + "#" + arr[x].username + "#" + arr[x].email);
//   }
//   for(item of arr){
//     console.log(item.name + "," + item.username + "," + item.email);
//   }
//   arr.forEach(item => {
//     console.log(item.name + "^" + item.username + "^" + item.email);
//   })
// }
// getData(users);