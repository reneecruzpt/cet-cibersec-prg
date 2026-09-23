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

lista1 = ['ABBA', '1231', 'morango', 'CET', '1231', 'osso', 2, 'p', 'tenet', 'tenet','reinier', 'Ana', 123, '7asd0', 2, 'p']
lista2 = [0, 0, 1, 2, 1, 3, 4, 5, 2, 4, 3, 5, 6, 7, 7, 8, 8, 9, 1, 0 ,9]

def contar_strings(lista):
    count = 0
    for item in lista:
        if isinstance(item, str) and len(item) >= 2 and item[0] == item[-1]:
            count += 1
    return count

resultado = contar_strings(lista1)
print("Número de strings com dimensão maior ou igual a 2 e com primeiro e último caractere iguais:", resultado)

def remover_duplicados(lista):
    return list(set(lista))

resultado = remover_duplicados(lista2)
print("Lista sem elementos duplicados:", resultado)

def remover_tipo(lista, tipo):
    nova_lista = []
    for item in lista:
        if not isinstance(item, type(tipo)):
            nova_lista.append(item)
    return nova_lista

tipo_removido = type(int(input("Digite o tipo a ser removido (0 para inteiros, 1 para strings, etc.): ")))
resultado = remover_tipo(lista1, tipo_removido)
print("Lista sem elementos do tipo especificado:", resultado)

def remover_tipo(lista, tipo):
    nova_lista = []
    for item in lista:
        if not isinstance(item, tipo):
            nova_lista.append(item)
    return nova_lista

tipo_removido = int(input("Digite o tipo a ser removido (0 para inteiros, 1 para strings, etc.): "))
resultado = remover_tipo(lista1, tipo_removido)
print("Lista sem elementos do tipo especificado:", resultado)

def contar_strings(lista):
    count = 0
    for item in lista:
        if isinstance(item, str) and len(item) >= 2 and item[0] == item[-1]:
            count += 1
    return count

resultado = contar_strings(lista1)
print("Número de strings com dimensão maior ou igual a 2 e com primeiro e último caractere iguais:", resultado)

