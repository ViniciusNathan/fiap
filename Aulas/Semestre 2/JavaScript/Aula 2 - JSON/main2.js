const emJSON = '{"id":2, "produto":"arroz"}'
const produto1 = JSON.parse(emJSON)

console.log(typeof emJSON);
console.log(typeof produto1);
console.log(produto1.produto); //arroz

const produto2 = JSON.parse(localStorage.getItem('produto1'));
console.log(produto2);


