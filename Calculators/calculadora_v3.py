'''
Calculadora Versão 3.0
Uma versão melhorada da Calculadora Ver. 2.0.
Utiliza Classes a fim de possibilitar a implementação de um sistema de login de utilizadores, onde cada utilizador possui password, palavra-passe e o seu histórico individual de operações.
Só é possível utilizar a calculadora após a realização do login.
Só é possível realizar o login após efetuar o registo.
Dev: Renee Cruz, 2024.
'''

class Utilizador:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        # Históricos individuais por operação
        self.historico_adicao = []
        self.historico_subtracao = []
        self.historico_multiplicacao = []
        self.historico_divisao = []
        self.historico_resto = []
        self.historico_potenciacao = []

    # Função para exibir histórico de uma operação específica
    def exibir_historico(self, operacao):
        if operacao == 'adição':
            lista = self.historico_adicao
        elif operacao == 'subtração':
            lista = self.historico_subtracao
        elif operacao == 'multiplicação':
            lista = self.historico_multiplicacao
        elif operacao == 'divisão':
            lista = self.historico_divisao
        elif operacao == 'resto da divisão':
            lista = self.historico_resto
        elif operacao == 'potenciação':
            lista = self.historico_potenciacao
        else:
            print("Operação inválida.")
            return

        if len(lista) == 0:
            print(f"Não há operações registradas para {operacao}.")
        else:
            print(f"\nHistórico de {operacao}:")
            for item in lista:
                print(item)

class SistemaCalculadora:
    def __init__(self):
        self.utilizadores = []  # Lista de utilizadores registados
        self.utilizador_atual = None  # Utilizador atualmente logado

    # Função para registar um novo utilizador
    def registar(self):
        nome = input("Digite o nome do utilizador: ")
        senha = input("Digite a palavra-passe: ")
        # Verifica se o nome já existe
        for utilizador in self.utilizadores:
            if utilizador.nome == nome:
                print("Nome de utilizador já existente. Tente outro.")
                return
        # Cria um novo utilizador
        novo_utilizador = Utilizador(nome, senha)
        self.utilizadores.append(novo_utilizador)
        print("Registo concluído com sucesso!")

    # Função para realizar login
    def login(self):
        nome = input("Digite o nome do utilizador:\n->")
        senha = input("Digite a palavra-passe:\n->")
        for utilizador in self.utilizadores:
            if utilizador.nome == nome and utilizador.senha == senha:
                self.utilizador_atual = utilizador
                print(f"Login efetuado com sucesso! Bem-vindo, {nome}.")
                return True
        print("Nome de utilizador ou palavra-passe incorretos.")
        return False

    # Função para logout
    def logout(self):
        self.utilizador_atual = None
        print("Logout efetuado com sucesso.")

    # Funções de operações
    def adicao(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

    def multiplicacao(self, x, y):
        return x * y

    def divisao(self, x, y):
        if y == 0:
            return "Erro: divisão por zero!"
        return x / y

    def resto(self, x, y):
        if y == 0:
            return "Erro: divisão por zero!"
        return x % y

    def potenciacao(self, x, y):
        return x ** y

    # Função principal da calculadora
    def calculadora(self):
        while True:
            print("\nEscolha a operação:")
            print("1 - Adição")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Resto da divisão")
            print("6 - Potenciação")
            print("7 - Exibir histórico de operações")
            print("8 - Logout")

            escolha = input("Digite o número da operação:\n->")

            if escolha == '8':
                self.logout()
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

                operacoes = {'1': 'adição', '2': 'subtração', '3': 'multiplicação', '4': 'divisão', '5': 'resto da divisão', '6': 'potenciação'}
                if escolha_hist in operacoes:
                    self.utilizador_atual.exibir_historico(operacoes[escolha_hist])
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
                resultado = self.adicao(num1, num2)
                print(f"Resultado: {resultado}")
                self.utilizador_atual.historico_adicao.append(f"{num1} + {num2} = {resultado}")
            elif escolha == '2':
                resultado = self.subtracao(num1, num2)
                print(f"Resultado: {resultado}")
                self.utilizador_atual.historico_subtracao.append(f"{num1} - {num2} = {resultado}")
            elif escolha == '3':
                resultado = self.multiplicacao(num1, num2)
                print(f"Resultado: {resultado}")
                self.utilizador_atual.historico_multiplicacao.append(f"{num1} * {num2} = {resultado}")
            elif escolha == '4':
                resultado = self.divisao(num1, num2)
                print(f"Resultado: {resultado}")
                self.utilizador_atual.historico_divisao.append(f"{num1} / {num2} = {resultado}")
            elif escolha == '5':
                resultado = self.resto(num1, num2)
                print(f"Resultado: {resultado}")
                self.utilizador_atual.historico_resto.append(f"{num1} % {num2} = {resultado}")
            elif escolha == '6':
                resultado = self.potenciacao(num1, num2)
                print(f"Resultado: {resultado}")
                self.utilizador_atual.historico_potenciacao.append(f"{num1} ** {num2} = {resultado}")

    # Função para iniciar o sistema
    def iniciar(self):
        while True:
            print("\nMenu Principal:")
            print("1 - Login")
            print("2 - Registo")
            print("3 - Encerrar")

            escolha = input("Escolha uma opção:\n->")

            if escolha == '1':
                if self.login():
                    self.calculadora()
            elif escolha == '2':
                self.registar()
            elif escolha == '3':
                print("Encerrando o sistema...")
                break
            else:
                print("Escolha inválida. Tente novamente.")

# Iniciar o sistema de calculadora
sistema = SistemaCalculadora()
sistema.iniciar()
