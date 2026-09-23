'''
Calculadora Versão 2.0
Uma versão melhorada da Calculadora Ver. 1.0.
Utiliza-se de listas a fim de possibilitar a implementação de um histórico individual para cada operação.
Dev: Renee Cruz, 2024.
'''
# Funções de operações
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x / y

def resto(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x % y

def potenciacao(x, y):
    return x ** y

# Função para exibir o histórico
def exibir_historico(operacao, lista):
    if len(lista) == 0:
        print(f"Não há operações registradas para {operacao}.")
    else:
        print(f"\nHistórico de {operacao}:")
        for item in lista:
            print(item)

# Função principal da calculadora
def calculadora():
    # Listas para armazenar os resultados
    historico_adicao = []
    historico_subtracao = []
    historico_multiplicacao = []
    historico_divisao = []
    historico_resto = []
    historico_potenciacao = []

    while True:
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Resto da divisão")
        print("6 - Potenciação")
        print("7 - Exibir histórico de operações")
        print("8 - Sair")

        escolha = input("Digite o número da operação:\n->")

        if escolha == '8':
            print("Encerrando a calculadora...")
            break

        if escolha == '7':
            print("\nEscolha o histórico que deseja ver:")
            print("1 - Adição")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Resto da divisão")
            print("6 - Potenciação")
            escolha_hist = input("Digite o número da operação para ver o histórico:\n->")

            if escolha_hist == '1':
                exibir_historico("adição", historico_adicao)
            elif escolha_hist == '2':
                exibir_historico("subtração", historico_subtracao)
            elif escolha_hist == '3':
                exibir_historico("multiplicação", historico_multiplicacao)
            elif escolha_hist == '4':
                exibir_historico("divisão", historico_divisao)
            elif escolha_hist == '5':
                exibir_historico("resto da divisão", historico_resto)
            elif escolha_hist == '6':
                exibir_historico("potenciação", historico_potenciacao)
            else:
                print("Escolha inválida.")
            continue

        if escolha not in ['1', '2', '3', '4', '5', '6']:
            print("Escolha inválida. Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número:\n->"))
            num2 = float(input("Digite o segundo número:\n->"))
        except ValueError:
            print("Erro: Por favor, insira números válidos!")
            continue

        if escolha == '1':
            resultado = adicao(num1, num2)
            print(f"Resultado: {resultado}")
            historico_adicao.append(f"{num1} + {num2} = {resultado}")
        elif escolha == '2':
            resultado = subtracao(num1, num2)
            print(f"Resultado: {resultado}")
            historico_subtracao.append(f"{num1} - {num2} = {resultado}")
        elif escolha == '3':
            resultado = multiplicacao(num1, num2)
            print(f"Resultado: {resultado}")
            historico_multiplicacao.append(f"{num1} * {num2} = {resultado}")
        elif escolha == '4':
            resultado = divisao(num1, num2)
            print(f"Resultado: {resultado}")
            historico_divisao.append(f"{num1} / {num2} = {resultado}")
        elif escolha == '5':
            resultado = resto(num1, num2)
            print(f"Resultado: {resultado}")
            historico_resto.append(f"{num1} % {num2} = {resultado}")
        elif escolha == '6':
            resultado = potenciacao(num1, num2)
            print(f"Resultado: {resultado}")
            historico_potenciacao.append(f"{num1} ** {num2} = {resultado}")

calculadora()
