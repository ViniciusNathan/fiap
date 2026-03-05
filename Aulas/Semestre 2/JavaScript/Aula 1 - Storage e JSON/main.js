localStorage.setItem('boas-vindas', 'Olá Dev!'); 
localStorage.setItem('valido', true);
localStorage.setItem('numero', 20);

let mensagem = localStorage.getItem('boas-vindas');
let valido = localStorage.getItem('valido');
let numero = localStorage.getItem('numero');

console.log(mensagem);
console.log(valido);
console.log(numero);

sessionStorage.setItem('selecionados', [1,2,3]);
sessionStorage.setItem('valido', false);

let lista = sessionStorage.getItem('selecionados').split(',');
let item = sessionStorage.getItem('valido') == true;

console.log(lista);
console.log(item)

//loop para percorrer as chaves armazenadas no objeto

for (let i = 0; i < localStorage.length; i++) {
    let chave = localStorage.key(i);
    console.log('Chave: ' + chave + " Valor: " + localStorage.getItem(chave));
    
}

//Eliminar dados

localStorage.removeItem('boas-vindas') //Elimina um item
localStorage.clear() //Elimina tudo