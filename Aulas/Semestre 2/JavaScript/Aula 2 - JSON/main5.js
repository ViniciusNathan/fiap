/*
Simule o armazenamento e recuperação de produtos de um carrinho de compras de uma loja online no localStorage

- Use um array para armazenar os produtos
- Para cada produto informe: id, nome, valor, quantidade
- Ao inicializar sua aplicação verifique se já produtos no carrinho
- Caso já existam produtos no carrinho, exiba esses produtos
- Caso não existam, exiba a mensagem "Carrinho vazio"
*/

const lista = [
    { id: 1, produto: 'Arroz', preco: 125 },
    { id: 2, produto: 'Macarrao', preco: 70 },
    { id: 3, produto: 'Pão', preco: 50 },
    { id: 4, produto: 'Pudim', preco: 100 },
]

const carrinho = []

let vazio = 'Carrinho vazio'