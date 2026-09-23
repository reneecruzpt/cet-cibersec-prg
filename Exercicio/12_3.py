#----------------------------------------------------------------------------------------
# Métodos das LISTAS
#
#  -Escreva um programa em Python que remova elementos do mesmo tipo de uma lista (colocar o tipo removido numa nova lista).
#  -Escreva um programa em Python que troque caracteres nos elementos de uma lista (pedir ao utilizador os caracteres a serem trocados).
#
# 28-02-2024, Renee Cruz
#---------------------------------------------------------------------------------------

lista1 = ['ABBA', '1231', 'morango', 'CET', '1231', 'osso', 2, 'p', 'tenet', 'tenet','reinier', 'Ana', 123, '7asd0', 2, 'p']
lista2 = [0, 0, 1, 2, 1, 3, 4, 5, 2, 4, 3, 5, 6, 7, 7, 8, 8, 9, 1, 0 ,9]


# Listas para armazenar elementos de tipos diferentes
listasPorTipo = []

# Percorrer os elementos da lista
for item in lista1:
    encontrado = False
    # Percorrer as listasPorTipo para verificar se o tipo do item já foi encontrado
    for listaTipo in listasPorTipo:
        if isinstance(listaTipo[0], type(item)):
            listaTipo.append(item)
            encontrado = True
            break
    if not encontrado:
        listasPorTipo.append([item])

# Imprimir as listas separadas por tipo
for listaTipo in listasPorTipo:
    tipo = type(listaTipo[0])
    print(f"Elementos do tipo {tipo}: {listaTipo}")
    
