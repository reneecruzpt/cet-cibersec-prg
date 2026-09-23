# ******************************************************************************************************************
# Escreva um programa em Python que dado uma lista de números inteiros os converte num único número inteiro.
# Exemplo: lista = [12, 45, 6, 23] N_int = 1245623
#
# Escreva um programa em Python que dado duas listas indique as diferenças entre elas.
# Exemplo: Lista1 = [‘vermelho’, ‘azul’, ‘verde’, ‘4’] Lista2 = [‘verde’, ‘5’, ‘azul’] Resultado: Lista3 = [‘vermelho’, ‘5’, ‘4’]
#
# Escreva um programa em Python que dado uma lista de números remove os repetidos consecutivos sem remover os repetidos.
# Exemplo: lista1 = [0, 0, 1, 2, 2, 3, 5, 5, 8, 2, 2] resultado: Lista2 = [0, 1, 2, 3, 5, 8, 2]
#
# Reneê Cruz, 12/03/2024
# ******************************************************************************************************************


#Exercício 1.1 - List Concatenation
print("\nExercício 1")
lista = [12, 45, 6, 23]
N_int = ""
print("Lista 1: {}".format(lista))
for element in lista:
    N_int += str(element)
total = int(N_int)
print("Número inteiro: {}".format(N_int))

#Exercício 1.2 - List Comprehension
# lista = [12, 45, 6, 23]
# myInt = ''.join(str(x) for x in lista)
# myInt = int(myInt)
# print(myInt)


#Exercício 2.1
print("\nExercício 2")
lista1 = ['vermelho', 'azul', 'verde', '4']
lista2 = ['verde', '5', 'azul']
lista3 = []

print("Lista 1: {}".format(lista1))
print("Lista 2: {}".format(lista2))

for element in lista1 + lista2: #Concatenação de listas
    if element not in lista1 or element not in lista2: #Verifica se os elementos não estão na lista 1 ou 2
        lista3.append(element)  #Adiciona os elementos na lista 3
print("Lista resultante: {}".format(lista3))

#Exercício 2.2
# lista1 = ['vermelho', 'azul', 'verde', '4']
# lista2 = ['verde', '5', 'azul']

# # Converte as listas em conjuntos (conjunto elemento único e não ordenado)
# set1 = set(lista1)
# set2 = set(lista2)

# # Encontra os elementos que estão em apenas um dos conjuntos
# lista3 = list(set1.symmetric_difference(set2))

# print("Lista resultante: {}".format(lista3))

#Exercício 3
print("\nExercício 3")
lista1 = [0, 0, 1, 2, 2, 3, 5, 5, 8, 2, 2]
lista2 = []
print("Lista raiz: {}".format(lista1))
for i in range(len(lista1)):
        if lista1[i] != lista1[i-1]:
            lista2.append(lista1[i])
print("Lista resultante: {}".format(lista2))
