#ciclos ou loops
#estruturas de repetição
#while ou enquanto é utilizado quando precisamos repetir uma ação n vezes, onde n é uma quantidade desconhecida de vezes
#ou seja por exemplo quando um utilizador acede a um menu em uma aplicação

print('Menu')
print('Opção 1')
print('Opção 2')
print('Opção 3')
op = input('Selecione uma opção de 1 a 3 (0 - para sair):\n->')

while op != '0': #avaliado uma expressão do tipo boolean, enquanto True (verdadeiro) execute a ação: 
    if op == '1': #True executa a ação, #False ignora a ação
        print('Você escolheu a opção 1')
    elif op == '2':
        print('Escolheste a opção 2')
    elif op == '3':
        print('Foi escolhida a opção 3')
    elif op == '0':
        print('Obrigado por utilizar a nossa aplicação!')
        break
    else:
        print('A opção escolhida:',op,', é inválida, por favor selecione uma opção válida.\n')

    print('Menu')
    print('Opção 1')
    print('Opção 2')
    print('Opção 3')
    op = input('Selecione uma opção de 1 a 3 (0 - para sair):\n->')

#linha a seguir ao loop
print('Obrigado por utilizar a nossa aplicação!')
#print('Fim.')