const produto1 = {id: 2, produto: 'Arroz'};
localStorage.setItem('produto1', produto1)

const emJSON = JSON.stringify(produto1) //converte em string

console.log(emJSON); //{"id":2, "produto":"Arroz"}
console.log(typeof produto1); //objeto
console.log(typeof emJSON); //string

localStorage.setItem('produto1', emJSON)
// É armazenado {"id":2, "produto":"Arroz"}


