class Produto { //A classe serve como um molde para criar objetos que representam produto
    constructor(obj) {
        this.nome = obj.produto.toUpperCase(); //Transforma em maiúscula
        this.preco = parseFloat(obj.preco);
    }
    somaICMS() {
        this.preco = this.preco * 1.21; //Calcula o preço com ICMS de 21%
    }
}

//Obtemos a lista de produtos armazenados
const armazenados = JSON.parse(localStorage.getItem('listaProdutos'));
const produtos = [];
//Iteramos os armazenados com for...of para transformar todos seus objetos no tipo produto
for (const objeto of armazenados)
    produtos.push(new Produto(objeto));
//Agora temos o objeto produtos e podemos usar seus métodos
for (const produto of produtos)
    produto.somaICMS;
//Armazenamos os produtos atualizados no localStorage
localStorage.setItem('listaProdutos', JSON.stringify(produtos))