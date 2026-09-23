# ******************************************************************************************************************
# Palíndromo é uma sequência de caracteres cuja leitura é igual quando feita da direita para esquerda ou vice−versa.
# Exemplo: OSSO e OVO são palíndromos.
# Reneê Cruz, 04/03/2024
# ******************************************************************************************************************

string = input("\nInsira uma string: ")

if len(string) < 2:
        print("A string deve ter pelo menos 2 caracteres.")
    
else :
    string_invertida = string[::-1]
    if string == string_invertida: # Verifica se é um palíndromo
        print("A string é um palíndromo: {}".format(string))
    else:
        print("A string não é um palíndromo: {}".format(string))
        

