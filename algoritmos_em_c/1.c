/*-----------------------------------------------------------------
Tarefa Parte 1 - 5059 
Este programa pede dois valores inteiros e com eles efetua várias operações
10-01-2024, Reneê Cruz
-------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>

void exibirMenu(){
    system("cls");
    printf("****************************************************************\n");
    printf("* Esta aplicação solicita ao utilizador dois valores inteiros. *\n");
    printf("***************** E efetua diversas operações: *****************\n");
    printf("***************** Somar, Subtrair e Multiplicar ****************\n");
    printf("*****************************************************************\n");
}

// Função para solicitar um número inteiro do usuário
int obterNumero(){
    int numeroUsuario; // Variável local

    printf("Introduza um número inteiro: ");
    scanf("%d", &numeroUsuario);

    return numeroUsuario;
}

// Função para realizar a operação de soma e exibir o resultado
void realizarSoma(int a, int b){
    int resultadoSoma;

    resultadoSoma = a + b;

    printf("A soma de %d com %d é %d\n", a, b, resultadoSoma);
}

// Função para realizar a operação de subtração e exibir o resultado
void realizarSubtracao(int a, int b){
    int resultadoSubtracao;

    resultadoSubtracao = a - b;

    printf("A subtração de %d com %d é %d\n", a, b, resultadoSubtracao);
}

// Função para realizar a operação de multiplicação e exibir o resultado
void realizarMultiplicacao(int a, int b){
    int resultadoMultiplicacao;

    resultadoMultiplicacao = a * b;

    printf("A multiplicação de %d com %d é %d\n", a, b, resultadoMultiplicacao);
}

int main(){
    int valorA, valorB;

    exibirMenu();
    valorA = obterNumero();
    valorB = obterNumero();

    realizarSoma(valorA, valorB);
    realizarSubtracao(valorA, valorB);
    realizarMultiplicacao(valorA, valorB);

    return 0;
}