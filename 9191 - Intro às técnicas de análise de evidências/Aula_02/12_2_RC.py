#----------------------------------------------------------------------------------------
# Métodos das LISTAS
#
#  -Escreva um programa em Python que conte o número de strings de uma dada lista,
#   a dimensão das strings tem de ser maior ou igual a 2 e o primeiro e último caractere
#   tem de ser igual.
#  -Escreva um programa em Python que remova elementos duplicados de uma lista.
#  -Escreva um programa em Python que remova elementos do mesmo tipo de uma lista (colocar o tipo removido numa nova lista).
#  -Escreva um programa em Python que troque caracteres nos elementos de uma lista (pedir ao utilizador os caracteres a serem trocados).
#
# 28-02-2024, Reneê Cruz
#---------------------------------------------------------------------------------------

# raw lists
lista1 = ['ABBA', '1231', 'morango', 'CET', '1231', 'osso', 2, 'p', 'tenet', 'tenet','reinier', 'Ana', 123, '7asd0', 2, 'p', True]
lista2 = [0, 0, 1, 2, 1, 3, 4, 5, 2, 4, 3, 5, 6, 7, 7, 8, 8, 9, 1, 0 ,9]

# Contagem de strings com dimensão maior ou igual a 2 e com primeiro e último caractere iguais
count_strings = 0
for item in lista1:
    if type(item) == str and len(item) >= 2 and item[0] == item[-1]:
        count_strings += 1
print("Número de strings com dimensão maior ou igual a 2 e com primeiro e último caractere iguais:", count_strings)

#utilizando set
# lista_sem_duplicados = list(set(lista2)) #com uma nova lista
# print("Lista sem elementos duplicados:",lista_sem_duplicados)

# lista2[:] = list(set(lista2)) #utilizando a mesma lista
# print("Lista sem elementos duplicados:",lista2)


# Remoção de elementos duplicados de uma lista
# nova_lista2 = []
# for item in lista2:
#     if item not in nova_lista2:
#         nova_lista2.append(item)
# print("Lista sem elementos duplicados:", nova_lista2)


# Remoção de elementos do mesmo tipo de uma lista
# tipo_removido = int(input("Digite o tipo a ser removido:\n0 para inteiros\n1 para strings\n2 para float\n3 para boolean\n-> "))
# nova_lista1 = []
# for item in lista1:
#     if (tipo_removido == 0 and type(item) != int) or (tipo_removido == 1 and type(item) != str) or (tipo_removido == 2 and type(item) != float) or (tipo_removido == 3 and type(item) != bool):
#         nova_lista1.append(item)
# print("Lista sem elementos do tipo especificado:", nova_lista1)

#Remoção utilizando pop na mesma lista, causa erros devido a lista estar em memória.
# tipo_removido = int(input("Digite o tipo a ser removido:\n0 para inteiros\n1 para strings\n2 para float\n3 para boolean\n-> "))
# for item in lista1:
#     if (tipo_removido == 0 and type(item) == int) or (tipo_removido == 1 and type(item) == str) or (tipo_removido == 1 and type(item) == float) or (tipo_removido == 1 and type(item) == bool):
#         lista1.remove(item)
# print("Lista sem elementos do tipo especificado:", lista1)

#itera sobre uma cópia da lista evitando problemas.
# tipo_removido = int(input("Digite o tipo a ser removido:\n0 para inteiros\n1 para strings\n2 para float\n3 para boolean\n-> "))
# for item in lista1[:]:
#     if (tipo_removido == 0 and type(item) == int) or (tipo_removido == 1 and type(item) == str) or (tipo_removido == 1 and type(item) == float) or (tipo_removido == 1 and type(item) == bool):
#         lista1.remove(item)
# print("Lista sem elementos do tipo especificado:", lista1)

# Contagem de strings novamente
# count_strings = 0
# for item in nova_lista1:
#     if type(item) == str and len(item) >= 2 and item[0] == item[-1]:
#         count_strings += 1
# print("Número de strings com dimensão maior ou igual a 2 e com primeiro e último caractere iguais:", count_strings)

count_strings = 0
for item in lista1:
    if type(item) == str and len(item) >= 2 and item[0] == item[-1]:
        count_strings += 1
print("Número de strings com dimensão maior ou igual a 2 e com primeiro e último caractere iguais:", count_strings)


# Substitui o caractere indicado pelo utilizador na lista
# char_antigo = input("Digite o caractere a ser substituído: ")
# char_novo = input("Digite o caractere substituto: ")
# for i in range(len(lista1)):
#     if type(lista1[i]) == str:
#         lista1[i] = lista1[i].replace(char_antigo, char_novo)

# print("Lista com caracteres trocados:", lista1)

#Troca entre caracteres
temp = '#_#_#'
char_antigo = input("Digite o caractere a ser substituído: ")
char_novo = input("Digite o caractere substituto: ")
for i in range(len(lista1)):
    if type(lista1[i]) == str:
        lista1[i] = lista1[i].replace(char_antigo, temp).replace(char_novo, char_antigo).replace(temp, char_novo)
print("Lista com caracteres trocados:", lista1)