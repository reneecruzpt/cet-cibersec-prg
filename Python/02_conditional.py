#estrutura condicional / decisão

# resposta = input('vamos ao parque?(s/n)\n-> ')
# resposta = resposta.lower()
# #print(resposta)
# if resposta == 'y':
#     print('Excelente! vou preparar os lanches!')
# # else:
# #     print('É uma pena, espero contar consigo na próxima oportunidade.')
# print('\nfim do programa')

print('Adivinhe o número')
num = 5
#guess = input('Entre um número:\n->')

guess = input('Entre um número:\n->')
if guess.isnumeric == True:
    print('Você entrou um número')
    if num == guess:
        print('você acertou!')
    if num != guess:
        print('você errou!')
else:
    print('Você não entrou um número')

#menu
# print('Menu')
# print('Opção 1')
# print('Opção 2')
# print('Opção 3')
# print('Opção 4')
# print('Opção 5')

# option = input('Sua opção -> ')

# if option == '1':
#     print('Você escolheu a opção 1')
#     #break
# if option == '2':
#     print('Você escolheu a opção 2')
#     #break
# if option == '3':
#     print('Você escolheu a opção 3')
#     #break
# if option == '4':
#     print('Você escolheu a opção 4')