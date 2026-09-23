# *******************************************************************************************************
# Escreva um programa em Python que receba uma lista de números e retorne a soma cumulativa;
# Isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i-1 elementos da lista original.
# Exemplo: lista = [1,2,3], ListaSum = [1,3,6]
# Reneê Cruz, 04/03/2024
# *******************************************************************************************************


lista = [1, 2, 3, 4, 5, 6] # raw list
lista_soma = [] # lista vazia para guardar os elementos somados

#estruturado
soma = 0 #variável temporária para guardar o valor da soma
for num in lista: # iterar sobre a raw list
    soma += num #somar o valor anterior com o valor atual
    lista_soma.append(soma) #adicionar o novo elemento a lista
print("Lista original:", lista) #imprimir a lista original
print("Lista com somas:", lista_soma) #imprimir a lista com somas

#compressão de lista
#lista_soma = [sum(lista[:i+1]) for i in range(len(lista))]
# sum(lista[:i+1]) - calcula a soma até a posição i (exclui i+1)
# range(len(lista)) - cria um iterável com os índices de 0 até o comprimento da lista menos 1.
# lista[:i+1] - fatia da lista até o elemento 'i-ésimo'

print("Lista original:", lista)
print("Lista com somas:", lista_soma)

#extra
#fibonacci - cada número da sequência é a soma de dois números anteriores
# fibonacci = [0, 1] #números iniciais da sequência

# n = int(input("Digite o número de elementos da sequência Fibonacci: ")) #entrada da quantidade de elementos

# for i in range(2, n): # a lista começa em dois, pois os dois primeiros elementos ja foram definidos
#     fibonacci.append(fibonacci[-1] + fibonacci[-2]) #(-1) último elemento + (-2) penúltimo elemento, são somados para calcular o próximo número da lista

# print("Sequência de Fibonacci com", n, "elementos:", fibonacci) #imprime o número de elementos e a sequência

