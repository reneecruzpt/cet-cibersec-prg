# def hello_1():
#     print('Olá mundo!')
    
# #hello_1()
    
# def hello_2(string):
#     print('Olá',string,'seja muito bem-vindo!')
    
#hello_2('Aluno')

#nome = input('Qual é o seu nome?\n->') + ','
#hello_2(nome)

# def soma_1():
#     resultado = 3 + 2
#     print(resultado)

# soma_1()

def soma_2(num1,num2):
    resultado = num1  + num2
    return resultado

#print('O resultado da soma_2 de 3 + 2 é: ',soma_2(3,2))

print('Bem vindo utilizador, este script calcula a soma de dois valores.')

valor_1 = input('Digite o primeiro valor\n->')
valor_2 = input('Digite o segundo valor\n->')

print('O resultado da soma_2 de',valor_1,'+',valor_2,'é: ',soma_2(valor_1,valor_2))

valor_1 = int(input('Digite o primeiro valor\n->'))
valor_2 = int(input('Digite o primeiro valor\n->'))

print('O resultado da soma_2 de',valor_1,'+',valor_2,'é: ',soma_2(valor_1,valor_2))