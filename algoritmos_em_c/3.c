#include <stdio.h>
#include <stdlib.h>

void menu(){
    system("cls");
    printf("**********************************************\n");
    printf("* Programa para pedir dois valores inteiros. *\n");
    printf("* Com estes valores efetua várias operações. *\n");
    printf("* 1. Soma                                    *\n");
    printf("* 2. Subtração                               *\n");
    printf("* 3. Multiplicação                           *\n");
    printf("* 4. Divisão                                 *\n");
    printf("**********************************************\n");
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
    while (b <= 0 || a <= 0) {
        printf("Erro! A divisão aceita apenas números inteiros positivos. Insira novos valores: ");
        scanf("%d %d", &a, &b);
    }

    float div;

    div = (float)a / b;

    printf("A divisão de %d por %d é %.2f\n", a, b, div);
}


main(){
    int numA, numB, opcao;

    menu();
    numA = numero();
    numB = numero();

    menu();
    printf("Escolha uma operação (1-4): ");
    scanf("%d", &opcao);

    switch (opcao) {
        case 1:
            soma(numA, numB);
            break;
        case 2:
            sub(numA, numB);
            break;
        case 3:
            mul(numA, numB);
            break;
        case 4:
            divi(numA, numB);
            break;
        default:
            printf("Opção inválida!\n");
            break;
    }

}
