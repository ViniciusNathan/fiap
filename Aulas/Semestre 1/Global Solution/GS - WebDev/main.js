function pegarDados() {
    const userName = document.getElementById('nome').value
    const cpf = document.getElementById('cpf').value
    const email = document.getElementById('email').value
    const skills = habilidades
    const interesse = document.querySelector('input[name="interest"]:checked')?.value || ''; // Captura o interesse selecionado
    const userData = [userName, cpf, email, skills, interesse]
    return userData
}

function validarFormulario() {
    const listUserData = pegarDados()
    console.log('Dados coletados:', listUserData);
    alert("Formulário enviado com sucesso");

    // Verifique se um interesse foi selecionado
    const interesse = document.querySelector('input[name="interest"]:checked');
    if (!interesse) {
        alert('Selecione um interesse');
        return;
    }
}

function checarEmail() {
    const userEmailInput = document.getElementById('email');
    const userEmailError = document.getElementById('userEmailError');

    if (userEmailInput.value.trim() === '') {
            userEmailError.textContent = 'e-mail é obrigatório';
            userEmailError.style.display = 'block';
        } else {
            userEmailError.style.display = 'none';
    }
}

function checarCPF() {
    const userCpfInput = document.getElementById('cpf');
    const userCpfError = document.getElementById('userCpfError');

    if (userCpfInput.value.trim() === '') {
            userCpfError.textContent = 'cpf é obrigatório';
            userCpfError.style.display = 'block';
        } else if (userCpfInput.value.length < 14) {
            userCpfError.textContent = 'campo incompleto';
            userCpfError.style.display = 'block';
        } else {
            userCpfError.textContent = '';
            userCpfError.style.display = 'none';
    }
}

function formatarCPF(mascara, valor) {
    const key = event.keyCode || event.which;
    // Permite apenas números (key codes 48-57) e algumas teclas especiais (Backspace, Tab, etc.)
    if (!((key >= 48 && key <= 57) || key === 8 || key === 9 || key === 46)) {
        event.preventDefault(); // Impede a entrada de letras
        return; // Sai da função se não for um número
    }

    const v = valor.value.replace(/\D/g, ''); // Remove caracteres não numéricos
    let i = 0;
    const resultado = mascara.replace(/#/g, () => v[i++] || ''); // Aplica a máscara
    valor.value = resultado; // Atualiza o valor do input
}

function exibirFeedback() {
    const userNameInput = document.getElementById('nome');
    const userNameError = document.getElementById('userNameError');

    if (userNameInput.value.trim() === '') {
        userNameError.textContent = 'nome é obrigatório';
        userNameError.style.display = 'block';
    } else {
        userNameError.textContent = '';
        userNameError.style.display = 'none';
    } 
}

let habilidades = []; // Array para armazenar as habilidades

function addHabilidades() {
    const skillsInput = document.getElementById('skillsInput');
    const userSkillsMessage = document.getElementById('userSkills');

    const habilidadeSelecionada = skillsInput.value.trim();

    if (habilidadeSelecionada === '') {
        alert('Selecione uma habilidade válida.');
        return;
    }

    if (habilidades.includes(habilidadeSelecionada)) {
        alert('Habilidade já adicionada.');
        return;
    }

    habilidades.push(habilidadeSelecionada); // Adiciona a habilidade ao array
    
    // Exibe as habilidades como uma lista no span
    userSkillsMessage.innerHTML = habilidades.map(h => `<div>${h}</div>`).join('');
    
    skillsInput.value = ''; // Limpa o campo de entrada
}