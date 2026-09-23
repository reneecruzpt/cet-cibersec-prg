#ciclo quando é necessário repetir uma operação n vezes, uma quantidade de vezes indefinida
#import os

#ciclo é necessário sempre quando desejamos repetir a operação várias vezes
#Servem para oferecer controle ao utilizador de quando quer encerrar a aplicação
#while = enquanto, enquanto determinada condição for verdadeira as ações que estão dentro do ciclo serão executadas

escolha = int(input('Digite um número:\n-> '))

while escolha != 0:
    print('Olá!\n')
    #escolha = int(input('Digite um número:\n-> '))

while True:
    #os.system('cls')
    print('Menu')
    print('Opção 1')
    print('Opção 2')
    print('Opção 3')
    print('Opção 4')
    print('Opção 5')
    
    option = input('Sua opção -> ')
    
    if option == '1':
        print('Você escolheu a opção 1')
        #break
    elif option == '2':
        print('Você escolheu a opção 2')
        #break
    elif option == '3':
        print('Você escolheu a opção 3')
        #break
    elif option == '4':
        print('Você escolheu a opção 4')
        #break
    # elif option == 5:
    #     print('Você escolheu a opção 5')
    #     break
    # elif int(option) == 5:
    #     print('Você escolheu a opção 5')
    #     break
    # elif option == '0':
    #     break
    else:
        print('Você não escolheu uma opção válida')
        
    input('Carregue enter para prosseguir')
    
print('Fim do programa')