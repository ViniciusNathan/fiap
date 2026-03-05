# Global Solution - O Futuro do Trabalho - Web Development

## Participantes

* Bruno - RM 568316
* Venicio - RM 568088
* Vinicius - RM 567105

## Sobre

O objetivo do formulário e coletar os dados iniciais de pessoas interessadas em buscar requalificações profissionais. Além dos dados pessoais, há dois campos para identificar as **habilidades** que o usuáiro possui e o **interesse** em temas sobre tecnologia.

## Código

- Dados
Para guardar os dados inseridos nos campos em variáveis foi criado a função `pegarDados()`

- Nome
O campo **Nome** possui a função `exibirFeedback()` onde valida se o campo foi preenchido, caso não tenha nenhum caractere é retornado uma mensagem `nome é obrigatório``

- CPF
O campo **CPF** possui 2 funções: 
`formatarCPF(mascara, valor)` para formatar considerando `xxx.xxx.xxx-xx` e só aceitando números
`checarCPF()` é a função que verifica se o campo foi preenchido e se o número de caracteres necessários foi preenchidos. São 14 caracteres 11 para os números e 3 para os pontos e hífen.

- Habilidades
O campo é de multi seleção e na função `addHabilidades()` ele pega cada item selecionado guarda em um vetor e mostra em tela os selecionados.

- Interesses
Neste campo as funções `pegarDados()` e `validarFormulario()` pegam o dado e verificam se um item foi selecionado no campo.

A função `validarFormulario()` é acionado ao clicar no botão **Enviar** e em seguida é uma alert aparece para confirmar o envio. No `Console` do navegador é possível ver o array.

##### Obrigado