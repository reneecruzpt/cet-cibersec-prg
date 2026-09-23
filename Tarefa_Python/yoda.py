'''
Script: Este script inverte a construção de uma frase e
retorna no ecrã um resultado semelhante ao que seria dito pelo personagem yoda. 

Dev: Reneê Cruz, 22/03/2024
'''

def yoda(texto):
    lista = texto.split(" ") #separa o texto em uma lista
    tamanho = len(lista) #verifica o tamanho da lista

    metade = tamanho // 2 #divisão inteira para obter a metade da lista
    if tamanho % 2 == 0: #verifica se o tamanho da lista é par
        lista1 = lista[:metade] #separa a lista com a primeira metade
        lista2 = lista[metade:] #separa a lista com a segunda metade
    else:
        lista1 = lista[:metade-1] #separa a lista com a primeira metade -1, faz mais sentido assim.
        lista2 = lista[metade-1:] #separa a lista com a segunda metade -1, faz mais sentido assim.
    
    string = " ".join(lista2)+ " " + " " .join(lista1) #atribui uma string com as listas invertidas
    return string #retorna a string



texto = input("Digite uma frase: ") #recebe a frase
print(yoda(texto)) #imprime o resultado



