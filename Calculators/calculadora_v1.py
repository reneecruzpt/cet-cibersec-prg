'''
Calculadora Versão 1.0
Um modelo simples com recurso a funções, possui um tratamento de erro para divisões por zero e um menu para o controle do fluxo da aplicação.
Dev: Renee Cruz, 2024.
'''
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

def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Resto da divisão")
        print("6 - Potenciação")
        print("0 - Sair")

        escolha = input("Digite o número da operação:\n->")

        if escolha == '0':
            print("Encerrando a calculadora...")
            break

        if escolha not in ['0', '1', '2', '3', '4', '5']:
            print("Escolha inválida. Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número:\n->"))
            num2 = float(input("Digite o segundo número:\n->"))
        except ValueError:
            print("Erro: Por favor, insira números válidos!")
            continue

        if escolha == '1':
            print(f"Resultado: {adicao(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(num1, num2)}")
        elif escolha == '5':
            print(f"Resultado: {resto(num1, num2)}")
        elif escolha == '6':
            print(f"Resultado: {potenciacao(num1, num2)}")

calculadora()
