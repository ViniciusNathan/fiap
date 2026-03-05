const produtos = [
    { id: 1, produto: 'Arroz', preco: 125 },
    { id: 2, produto: 'Macarrao', preco: 70 },
    { id: 3, produto: 'Pão', preco: 50 },
    { id: 4, produto: 'Pudim', preco: 100 },
]

const armazenarLocal = (chave, valor) => {localStorage.setItem(chave, valor)};

//Armazenar produto por produto
for (const produto of produtos) {
    armazenarLocal(produto.id, JSON.stringify(produto))
}

//ou armazenar array completo
armazenarLocal("listaProdutos", JSON.stringify(produtos))