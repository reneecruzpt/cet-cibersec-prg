# *******************************************************************************************************
# Conta vogais - Dado uma string introduzida pelo utilizador (incluindo espaços em branco), conta quantas vezes aparecem as vogais a, e, i, o, u
# Reneê Cruz, 04/03/2024
# *******************************************************************************************************


minha_string = "Não há razão para qualquer indivíduo ter um computador em casa"
print(minha_string + "\n")
# contador =  0

# for element in minha_string:
#     if element == "a" or element == "e" or element == "i" or element == "o" or element == "u":
#         contador += 1

# print("A quantidade total de vogais contadas é: {}\n".format(contador))


# vogaisMaiusculas = 0
# vogaisMinusculas = 0

# for element in minha_string:
#     if element == "A" or element == "E" or element == "I" or element == "O" or element == "U":
#         vogaisMaiusculas += 1
#     if element == "a" or element == "e" or element == "i" or element == "o" or element == "u":
#         vogaisMinusculas += 1

# print("A quantidade total de vogais maiúsculas contadas é: {}\n".format(vogaisMaiusculas))
# print("A quantidade total de vogais minúsculas contadas é: {}\n".format(vogaisMinusculas))    

#utilizando variáveis
# a = A = e = E = i = I = o = O = u = U = 0

#sem acentuação
# for element in minha_string:
#     if element == "a":
#         a += 1
#     elif element == "e":
#         e += 1
#     elif element == "i":
#         i += 1
#     elif element == "o":
#         o += 1
#     elif element == "u":
#         u += 1
#     if element == "A":
#         A += 1
#     elif element == "E":
#         E += 1
#     elif element == "I":
#         I += 1
#     elif element == "O":
#         O += 1
#     elif element == "U":
#         U += 1

#com acentuação
# for element in minha_string:
#     if element == "a" or element == "á" or element == "à" or element == "ã":
#         a += 1
#     elif element == "e" or element == "é" or element == "ê":
#         e += 1
#     elif element == "i" or element == "í":
#         i += 1
#     elif element == "o" or element == "ó" or element == "õ" or element == "ô":
#         o += 1
#     elif element == "u" or element == "ú":
#         u += 1
#     if element == "A" or element == "Á" or element == "À" or element == "Ã":
#         A += 1
#     elif element == "E" or element == "É":
#         E += 1
#     elif element == "I" or element == "Í":
#         I += 1
#     elif element == "O" or element == "Ó" or element == "Õ":
#         O += 1
#     elif element == "U" or element == "Ú":
#         U += 1
        
# print("A quantidade total de vogais \"a\" minúsculas contadas é de: {} e maiúsculas \"A\" contadas é de: {}\n".format(a,A))
# print("A quantidade total de vogais \"e\" minúsculas contadas é de: {} e maiúsculas \"E\" contadas é de: {}\n".format(e,E))
# print("A quantidade total de vogais \"i\" minúsculas contadas é de: {} e maiúsculas \"I\" contadas é de: {}\n".format(i,I))
# print("A quantidade total de vogais \"o\" minúsculas contadas é de: {} e maiúsculas \"O\" contadas é de: {}\n".format(o,O))
# print("A quantidade total de vogais \"u\" minúsculas contadas é de: {} e maiúsculas \"U\" contadas é de: {}\n".format(u,U))

#utilizando uma lista
# contagem_vogais = [0] * 10 

# vogais = "aeiouAEIOU"

# for element in minha_string:
#     if element in vogais:
#         indice = vogais.index(element)
#         contagem_vogais[indice] += 1

# for i in range(5):
#     print(f"A quantidade total de vogais \"{vogais[i]}\" minúsculas contadas é de: {contagem_vogais[i]} e maiúsculas \"{vogais[i+5]}\" contadas é de: {contagem_vogais[i+5]}\n")

    
#utilizando diversas acentuações
vogal_a = "aáàã"
vogal_e = "eéê"
vogal_i = "ií"
vogal_o = "o,ó,ô"
vogal_u = "u,ú"

contagem_vogais = [0] * 5 
for element in minha_string:
    if element in vogal_a:
        contagem_vogais[0] += 1
    elif element in vogal_e:
        contagem_vogais[1] += 1
    elif element in vogal_i:
        contagem_vogais[2] += 1
    elif element in vogal_o:
        contagem_vogais[3] += 1
    elif element in vogal_u:
        contagem_vogais[4] += 1
        
print("Contagem de vogais:\na: {}\ne: {}\ni: {}\no: {}\nu: {}".format(contagem_vogais[0],contagem_vogais[1],contagem_vogais[2],contagem_vogais[3],contagem_vogais[4],))

#utilização de duas listas e enumeração
vogais = ["aáàã", "eéê", "ií", "oóô", "uú"]

contagem_vogais = [0] * 5 

for element in minha_string:
    for i, vogal in enumerate(vogais): #enumerate adiciona um contador e torna o objeto em um objeto iterável numerado
        if element in vogal:
            contagem_vogais[i] += 1

print("\nContagem de vogais:\na: {}\ne: {}\ni: {}\no: {}\nu: {}".format(*contagem_vogais))

# Utilizando um dicionário
# contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

# for element in minha_string:
#     if element.lower() in contagem_vogais:
#         contagem_vogais[element.lower()] += 1

# for vogal, contagem in contagem_vogais.items():
#     if vogal.islower():
#         print(f"A quantidade total de vogais \"{vogal}\" minúsculas contadas é de: {contagem}")
#     else:
#         print(f"A quantidade total de vogais \"{vogal}\" maiúsculas contadas é de: {contagem}")
