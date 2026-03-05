

function calcular() {
    //Pega o elemento DOM do campo Inicio
    let inicioHora = document.getElementById("horaIni")
    let inicioMinutos = document.getElementById("minIni")

    //Pega o elemento DOM do campo Termino
    let terminoHora = document.getElementById("horaFim")
    let terminoMinuto = document.getElementById("minFim")

    //Guarda o dado em uma variavel Inicio e converte para Int
    let elementInicioHora = parseInt(inicioHora.value)
    let elementInicioMinutos = parseInt(inicioMinutos.value)

    //Guarda o dado em uma variavel Termino e converte para Int
    let elementTerminoHora = parseInt(terminoHora.value)
    let elementTerminoMinutos = parseInt(terminoMinuto.value)

    // Validação de entrada
    if (isNaN(elementInicioHora) || isNaN(elementInicioMinutos) || 
        isNaN(elementTerminoHora) || isNaN(elementTerminoMinutos)) {
        alert("Por favor, preencha todos os campos com números válidos");
        return;
    }

    // Validação de intervalos
    if (elementInicioHora < 0 || elementInicioHora > 23 || 
        elementTerminoHora < 0 || elementTerminoHora > 23 ||
        elementInicioMinutos < 0 || elementInicioMinutos > 59 ||
        elementTerminoMinutos < 0 || elementTerminoMinutos > 59) {
        alert("Por favor, insira horários válidos (0-23 horas, 0-59 minutos)");
        return;
    }
    
    //converte tempo inicio em minutos
    let convertInicio = (elementInicioHora * 60) + elementInicioMinutos

    //converte tempo termino em minutos
    let convertTermino = (elementTerminoHora * 60) + elementTerminoMinutos

    //Diferença de tempo entre Termino e Inicio
    let calcTempoMinutos = convertTermino - convertInicio

    // Se o resultado for negativo, significa que a reunião passou para o próximo dia
    if (calcTempoMinutos < 0) {
        // Adiciona 24 horas em minutos (24 * 60 = 1440)
        calcTempoMinutos += 1440;
    }

    //Converter as horas
    let convertHoras = parseInt(calcTempoMinutos / 60)

    //Converte os minutos
    let convertMinutos =  calcTempoMinutos - (convertHoras * 60)

    //Função para adicionar zero à esquerda
    function adicionarZero(num) {
        return num.toString().padStart(2, '0');
    }

    //Escreve Horas
    let trocaHoras = document.getElementById("horas")
    trocaHoras.innerText = adicionarZero(convertHoras)

    //Escreve Minutos
    let trocaMinutos = document.getElementById("minutos")
    trocaMinutos.innerText = adicionarZero(convertMinutos)

}


