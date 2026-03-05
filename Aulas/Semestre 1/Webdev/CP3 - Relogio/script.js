const today = new Date() // new Date() cria um objeto que pode ser modificado

let countSeconds = today.getSeconds() // Pega os segundos de new Date()
let countMinutes = today.getMinutes() // Pega os minutos de new Date()
let countHours = today.getHours() // Pega as horas de new Date()



let seconds = document.getElementById('segundos') //Guarda em uma variável o elemente segundos html
let minutes = document.getElementById('minutos')
let hours = document.getElementById('horas')


setInterval(() => {
    countSeconds++  
    if (countSeconds > 59) {
        countSeconds = 0
        countMinutes++
        if (countMinutes > 59) {
            countMinutes = 0
            countHours++
            if (countHours >= 24) {
                countHours = 0
            }
        }
    }
    seconds.innerText = String(countSeconds).padStart(2, '0')
    minutes.innerText = String(countMinutes).padStart(2, '0')
    hours.innerText = String(countHours).padStart(2, '0')
},1000)