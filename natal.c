#include <stdio.h>
#include <windows.h>

void imprimirArvore() {
    int linhas = 5;

    for (int i = 1; i <= linhas; i++) {

        for (int j = 0; j < linhas - i; j++) {
            printf(" ");
        }
        for (int k = 0; k < 2 * i - 1; k++) {
            if (i == 1) {
                printf("\x1b[33m*\x1b[0m");
            } else {
                printf("\x1b[32m*\x1b[0m");
            }
        }
        printf("\n");
    }
    printf("\x1b[31m   ***   \x1b[0m");
}


void piscarArvore() {
    while (1) {
        imprimirArvore();
        fflush(stdout);
        Sleep(500);

        system("cls");
        Sleep(500);
    }
}


void beep(int frequencia, int duracao) {
    Beep(frequencia, duracao);
}


void tocarNota(int nota, int duracao) {
    beep(nota, duracao);
    Sleep(200);
}
void pausa() {
    Sleep(200);
}

void jingleBells(){
    int Mi = 329;  
    int Sol = 392; 
    int Do = 261;  
    int Re = 293;  
    int Fa = 349;  

    int j;
    for (j = 0; j < 4; j++) {  
        int i;
        for (i = 0; i < 27; i++) {  
            tocarNota(Mi, 200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 400);
            Sleep(200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 400);
            Sleep(200);
            tocarNota(Mi, 200);
            tocarNota(Sol, 200);
            tocarNota(Do, 200);
            tocarNota(Re, 200);
            tocarNota(Mi, 400);
            Sleep(200);
            tocarNota(Fa, 200);
            tocarNota(Fa, 200);
            tocarNota(Fa, 400);
            Sleep(200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 400);
            Sleep(200);
            tocarNota(Re, 200);
            tocarNota(Mi, 200);
            tocarNota(Re, 200);
            tocarNota(Mi, 200);
            tocarNota(Sol, 400);
            Sleep(200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 400);
            Sleep(200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 400);
            Sleep(200);
            tocarNota(Mi, 200);
            tocarNota(Sol, 200);
            tocarNota(Do, 200);
            tocarNota(Re, 200);
            tocarNota(Mi, 400);
            Sleep(200);
            tocarNota(Fa, 200);
            tocarNota(Fa, 200);
            tocarNota(Fa, 400);
            Sleep(200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 200);
            tocarNota(Mi, 400);
            Sleep(200);
            tocarNota(Sol, 200);
            tocarNota(Fa, 200);
            tocarNota(Mi, 200);
            tocarNota(Re, 200);
            tocarNota(Do, 500);
        }
    }
}


int main() {
    printf("Pressione Ctrl+C para sair\n");


    HANDLE threadHandle = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)piscarArvore, NULL, 0, NULL);

    jingleBells();


    WaitForSingleObject(threadHandle, INFINITE);

    return 0;
}
