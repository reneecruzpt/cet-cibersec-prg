#o ciclo for é utilizado quando temos uma quantidade limitade de opções ou
#quando eu sei exatamente qual a quantidade de operações que eu quero realizar
#por exemplo o número de tentativas para a entrada de uma senha(palavra-passe)/password.

#cada vez que é verificada a condição de um ciclo nos temos uma iteração

# n = 3
# # password = input('Preencha com a sua password:\n->') #string

# pw = '0000' #string
# #pw = '' #mínimo de caracteres 12, maísculas, minúsculas, símbolos e números (que não sejam sequências ex: 1245, nem repetições: 111)

# chances = 3 #contador (counter)

# for iteracao in range(n): #n é exclusivo, o n não faz parte das iterações 0,1,2 o 3 fica de fora.
#     password = input('Preencha com a sua password:\n->') #string
#     if password == pw: #comparação de verdadeiro ou falso, número == string
#         print('A palavra passe está correta')
#         break
#     else:
#         print('Palavra passe incorreta')
#         print('Tentativa',iteracao + 1,'/',n)
#         if iteracao == 2:
#             print('Tentativas esgotadas!')

# nome = 'maria' #[m][a][r][i][a] uma cadeia de caracteres que inicia no índice 0
#                #[0][1][2][3][4]
# print(nome)

# for letra in nome: #para cada letra em nome, fazer:
#     print(letra)

# for letra in nome:
#     print(letra,end='')

# print()
# lista = ['maria','ana','rute','iris','amanda']

# for item in lista:
#     print(item)

#descobrir se existe um símbolo proibido em uma palavra

palavra = input('Entre uma palavra\n-> ')

proibido = '@'

if proibido in palavra:
    print('A palavra contém um símbolo proibido')
else:
    print('A palavra foi aceite')
    
# for letra in palavra:
#     if letra == proibido:
#         print('A palavra contém um símbolo proibido')
#         palavra = '' # == comparação / = atribuição
#         break

# if palavra != '':
#     print('A palavra foi aceite')
