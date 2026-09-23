# ******************************************************************************************************************
# Palíndromo é uma sequência de caracteres cuja leitura é igual quando feita da direita para esquerda ou vice−versa.
# Exemplo: OSSO e OVO são palíndromos.
# Reneê Cruz, 04/03/2024
# ******************************************************************************************************************
#Palíndromo 1 - String inserida pelo utilizador
while True: #loop adicionado para garantir que o utilizador cumpra os requisitos
    string = input("\nInsira uma string: ")
    
    if len(string) < 2: #verificação do tamanho da string
            print("A string deve ter pelo menos 2 caracteres. Por favor, Tente novamente.")
    else :
        for char in string:
            if char.isnumeric(): #verificação de números
                print("Um palíndromo não pode conter números. Por favor, Tente novamente.")
                break
        else:
            string_invertida = string[::-1]
            if string == string_invertida: # Verifica se é um palíndromo
                print("A string é um palíndromo: {}".format(string))
            else:
                print("A string não é um palíndromo: {}".format(string))
                
        resposta = input("Deseja verificar outra string? [S/N] ").strip().lower() #pergunta para o usuário se deseja virificar outra string
        
        if resposta != 's':
            print("Obrigado por utilizar este programa. Volte sempre!")
            break

#Palíndromo 2 - Lista predefinida

