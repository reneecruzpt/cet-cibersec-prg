#o que são funções?
#São trechos que código que podem ser reutilizados e que possuem um nome próprio
#Como por exemplo: print() -> imprimir no ecrã, input() -> recebe dados do utilizador no formato string 

#print()
#input()

#criar as nossas próprias funções, e o que precisamos para criar as nossas funções?
#da palavra reservada/palavra-chave "def" que significa define function 
#do nome da função, que não pode ser uma palavra reservada, com a inicial minúscula e quando necessário utilizamos o snake case
#snake_case: palavras sempre com as iniciais minúsculas e o separador é um underscore (_)

def hello(): #definição da função
    print('Hello World!') #ação da função
    print('Bem-vindo!')
    
#hello() #chamado da função ou #call function é como se fosse uma seta que aponta para a função, neste caso indica ao interpretador para executar o código definido na linha 13

def hello_2(string): #dentro dos parentesis podemos passar valores conhecidos como parâmetros ou argumentos
    print("Olá",string,'seja muito bem-vindo!')

# name = input('Escreva seu nome:\n-> ')
# hello_2(name) #chamado

def soma(valor1,valor2):
    resultado = int(valor1) + int(valor2)
    return resultado

valor1 = input('Insira o primeiro valor\n-> ') #todos os valores que recebemos através da função input são strings
valor2 = input('Insira o segundo valor\n-> ') #se nos predendermos utilizar esses valores para operações matemáticas, temos de realizar a conversão

valor_da_soma = soma(valor1,valor2)

print('A soma de',valor1,'+',valor2,'é igual a:',valor_da_soma)

