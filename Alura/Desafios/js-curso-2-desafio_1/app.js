let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

function exibirMensagemNoConsole() {
    console.log('O botão foi clicado');
}
function exibirAlerta() {
    alert('Eu amo JS');
}
function exibirPrompt() {
    let nomeCidade = prompt('Digite o nome de uma cidade do Brasil que você gosta muito');
    alert(`Estive em ${nomeCidade} e lembrei de você`);
}
function somaDoisNumeros() {
    let num1 = parseInt(prompt('Digite um número'));
    let num2 = parseInt(prompt('Digite outro número'));
    let somaNumero = num1 + num2;
    alert(`A soma entre ${num1} e ${num2} é igual a ${somaNumero} `);
}

function calcularIMC (altura, peso){
    let imc = peso / (alturaMetros * alturaMetros)
}
