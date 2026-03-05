//Atbash

function cifrarAtbash(texto) {
    let alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
    let alphaLower = 'abcdefghijklmnopqrstuvwyz'
    let saida = ''
    for(let i=0; i<texto.length; i++) {
        // console.log('letra: ', texto[i]);
        let letterIn = texto[i];
        let letterOut = ' '
        if (letterIn != ' ') {
            let position = alphaUpper.search(letterIn)
            if (position != -1) {
                letterOut = alphaUpper[alphaUpper.length - position - 1];
            } else {
                position = alphaLower.search(letterIn)
                letterOut = alphaLower[alphaLower.length - position - 1];
            }
        }
        // console.log('letraOut:', letterOut);
        saida = saida + letterOut
    }
    // console.log(saida);
    return saida
}

let cifrado = cifrarAtbash('ALfACE')
console.log('Cifrado', cifrado);
let decifrado = cifrarAtbash(cifrado)
console.log('Decifrado', decifrado);

// String.fromCharCode