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

int numero(){
    int num1; // variável local

    printf("Introduza um número inteiro: ");
    scanf("%d", &num1);

    return(num1);
}

void soma(int a, int b){
    int sum;

    sum = a + b;

    printf("A soma de %d com %d é %d\n", a, b, sum);
}

void sub(int a, int b){
    int sub;

    sub = a - b;

    printf("A subtração de %d com %d é %d\n", a, b, sub);
}

void mul(int a, int b){
    int mul;

    mul = a * b;

    printf("A multiplicação de %d com %d é %d\n", a, b, mul);
}

void divi(int a, int b){
    while (b == 0) {
        printf("Erro! O divisor não pode ser zero. Insira um novo valor para o divisor: ");
        scanf("%d", &b);
    }

    float div;

    div = (float)a / b;

    printf("A divisão de %d por %d é %.2f\n", a, b, div);
}

main(){
    int numA, numB;

    menu();
    numA = numero();
    numB = numero();

    soma(numA, numB);
    sub(numA, numB);
    mul(numA, numB);
    divi(numA, numB);

}
