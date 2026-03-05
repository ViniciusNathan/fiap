//opção 1 de como criar função
function fazAlgo(coisa) {
    console.log('faz algo', coisa);
    return 'oi' + coisa
}

//opção 2 de como criar função
let fazOutraCoisa = function(coisa) {
    console.log('faz outra coisa', coisa);
    return ''
}

let demoraMuito = function() { //Funções podem ser armazenadas em variáveis
    for(let i=0; i<1000000000; i++) {

    }
}

function misterio(algo) {
    console.log('mistério...');
    algo()
    //fazAlgo()
}

misterio(function() { //Função anônima
    console.log('anônima')
})

let pera = () => { 
    console.log('pera')
}

misterio(() => { //Arrow function
    console.log('pera')
})

let qtd = 0
function bomDia() {
    console.log('Bom dia', qtd);
    qtd++
}

let elem = document.getElementById('contador')

setInterval(() => {
    qtd++
    elem.innerText = qtd
},1000)

setTimeout(bomDia,3000)

setTimeout(() => {
    qtd = qtd + 50

},3000)

setInterval(bomDia,1000)

console.log('terminou')

// function banana() {
//     console.log('banana')
// }

// demoraMuito()


//misterio(fazOutraCoisa) //chamando uma função dentro do parâmetro de outra função

// fazAlgo(56)
// let resp = fazAlgo(56)
// console.log(resp)

// let f = fazAlgo
// console.log(f)
// f(55) //chamou a função 'Faz Algo'
// fazOutraCoisa('ABC')