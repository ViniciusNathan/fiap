// Repetição por contagem

let i = 1

while (i < 10) {
    console.log('oi', i)
    i++
}

//Início, condição e passo em uma linha
for (let i = 100; i >= 1; i--) {
    console.log('tchau')
}

// imprime números pares de 2 a 50
for (let i = 2; i < 51; i = i + 2) {
    console.log(i)
}

//Repetição por condicinal

let op = 'sim'

while (op == 'sim') {
    op = prompt('Quer continuar?')
}

let op1 = ""
while (op1 != "0") {
    op1 = prompt(`
            0 - SAIR
            1 - INCLUIR
            2 - PESQUISAR
            3 - EXCLUIR
            DIGITE UMA OPÇÃO:
        `)
}

