# ******************************************************************************************************************
# Adicione as palavras numa lista e extrai as string de uma determinada dimensão (pedida ao utilizador) para outra lista. 
#
# Reneê Cruz, 12/03/2024
# ******************************************************************************************************************


string = '''E também as memórias gloriosas
Daqueles Reis, que foram dilatando
A Fé, o Império, e as terras viciosas
De África e de Ásia andaram devastando;
E aqueles, que por obras valerosas
Se vão da lei da morte libertando;
Cantando espalharei por toda parte,
Se a tanto me ajudar o engenho e arte.'''

#Versão 1

# lista = string.replace(',', '').replace(';', '').replace('.', '').split(' ')
# palavras_encontradas = 0

# while True:
#     try:
#         size = int(input("Digite a dimensão da palavra (0 - para sair):\n->"))
#         if size == 0:
#             break  
#         for element in lista:
#             if len(element) == size:
#                 palavras_encontradas += 1
#                 print(element)
#         if palavras_encontradas == 0:
#             print("Nenhuma palavra com a dimensão especificada foi encontrada")
#         else:
#             if palavras_encontradas == 1:
#                 print("Foi encontrada {} palavra com a dimensão especificada".format(palavras_encontradas))
#             else:
#                 print("Foram encontradas {} palavras com a dimensão especificada".format(palavras_encontradas))
#     except:
#         print("Entrada inválida, Por favor digite um número inteiro\n") 

#Versão 2

# lista = []
# palavra = "" #utilizado para construir a palavra
# for caractere in string:
#   if caractere.isalnum(): #diz quando parar de incrementar a palavra
#     palavra += caractere #incrementa a palavra
#   else:
#     if palavra: # verifica se a palavra não está vazia antes de adicioná-la à lista
#             lista.append(palavra)
#             palavra = "" # reseta a variável

# size = int(input("Digite a dimensão da palavra:\n->"))
# for element in lista:
#     if len(element) == size:
#         print(element)
    

#Versão 3
# lista = []
# palavra = "" #utilizado para construir a palavra
# for caractere in string:
#   if caractere == " " or caractere == "\n" or caractere == ";" or caractere == "," or caractere == ".": #diz quando parar de incrementar a palavra
#     lista.append(palavra) #adiciona a palavra à lista
#     palavra = "" #reseta a variável
#   else:
#     palavra += caractere #incrementa a palavra

# lista.append(palavra)
# print(lista)

# size = int(input("Digite a dimensão da palavra:\n->"))
# for element in lista:
#     if len(element) == size:
#         print(element)

#Versão 4
# lista = []
# palavra = ""
# regex = [" ", "\n", ";", ",", "."]
# for caractere in string:
#     if caractere in regex:
#         if palavra:  # adiciona a palavra à lista se não for vazia
#             lista.append(palavra)
#             palavra = ""
#     else:
#         palavra += caractere

# if palavra:# adiciona a última palavra à lista se não for vazia
#     lista.append(palavra)

# size = int(input("Digite a dimensão da palavra:\n->"))
# for element in lista:
#     if len(element) == size:
#         print(element)

#Versão 5

nova_lista = []

for elemento in string.split():  # dividir a string em palavras
    if elemento[-1].isalnum():  # verifica se o último caractere é alfanumérico
        nova_lista.append(elemento)
    else:
        nova_lista.append(elemento[:-1])

#print("Lista original:", string.split())
#print("Nova lista sem o último caractere especial:", nova_lista)


size = int(input("Digite a dimensão da palavra:\n->"))
for element in nova_lista:
    if len(element) == size:
        print(element)