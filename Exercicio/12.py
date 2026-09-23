#----------------------------------------------------------------------------------------
# Métodos das LISTAS
#
#  -Escreva um programa em Python que conte o número de strings de uma dada lista,
#   a dimensão das strings tem de ser maior ou igual a 2 e o primeiro e último caractere
#   tem de ser igual.

#  -Escreva um programa em Python que remova os elementos duplicados de uma lista.

#  -Escreva um programa em Python que troque os caracteres nos elementos de uma lista.

# -
# 28-02-2024, Renee Cruz
#---------------------------------------------------------------------------------------

lista1 = ['ABBA', '1231', 'morango', 'CET', '1231', 'osso', 2, 'p', 'tenet', 'tenet', 'reinier', 'Ana', 123, '7asd0', 2, 'p']
lista2 = [0, 0, 1, 2, 1, 3, 4, 5, 2, 4, 3, 5, 6, 7, 7, 8, 8, 9, 1, 0, 9]

listasPorTipo = {}

for item in lista1:
    tipo = type(item)
    if tipo in listasPorTipo:
        listasPorTipo[tipo].append(item)
    else:
        listasPorTipo[tipo] = [item]


for tipo, listaTipo in listasPorTipo.items():
    print(f"Elementos do tipo {tipo}: {listaTipo}")
    

def trocarCaracteres(lista, caractereAntigo, caractereNovo):
    for i in range(len(lista)):
        if isinstance(lista[i], str):
            lista[i] = lista[i].replace(caractereAntigo, caractereNovo)


caractereAntigo = input("Digite o caractere a ser substituído: ")
caractereNovo = input("Digite o caractere que substituirá o caractere definido na primeira opção: ")

trocarCaracteres(lista1, caractereAntigo, caractereNovo)

print("Lista com caracteres trocados:", lista1)