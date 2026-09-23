'''
Tarefa de Avaliação: Python - CET Cibersegurança - Formador: Paulo Rodrigues

Script: Este é um sistema de registo e análise de notas de alunos.
        Ele permite registrar alunos com suas respectivas notas, calcular estatísticas como média, maior e menor nota,
        também permite realizar operações como exclusão de alunos, e exibição de alunos não validados.
        O utilizador interage com o sistema através de um menu simples e intuitivo.

Formando: Reneê Cruz, 22/03/2024
'''

import os

#Mensagem inicial
def introducao():
    print('''****************************************************************
Bem vindo ao sistema Ciberseg para registo de alunos e notas.
O sistema permite inserir nomes de alunos e atribuir notas,
após as atribuições é possível realizar as seguintes operações:

************* Mostrar os nomes dos alunos **********************
******* Mostrar os nomes dos alunos e as notas *****************
********************* Remover alunos ***************************
**************** Calcular a soma das notas *********************
**************** Encontrar a maior nota ************************
**************** Encontrar a menor nota ************************
******************* Calcular a média ***************************
****** Contar a quantidade de alunos acima da média geral ******
*** Contar a quantidade de alunos abaixo da nota de corte 9.5 **
****************************************************************
''')
    
    
#Regista alunos e notas
def registar_aluno_notas(nomes,notas):
    nome = ler_nome()
    notas_aluno = ler_notas()
    nomes.append(nome)
    notas.append(notas_aluno)
    print("Concluído! Aluno: {}, registado com sucesso.".format(nome))

#Apresenta o menu principal    
def main_menu():
    print("-" * 40)
    print("Menu Principal:")
    print("1.  Nome dos alunos")
    print("2.  Nome e notas")
    print("3.  Eliminar")
    print("4.  Soma dos elementos")
    print("5.  O maior elemento")
    print("6.  O menor elemento")
    print("7.  Média dos elementos")
    print("8.  Acima da média")
    print("9.  Elementos negativos (menores que 9,5)")
    print("10. Sair")
    print("-" * 40)


#Obtém a opcao escolhida pelo utilizador
def obter_opcao():
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida!")
        return obter_opcao()
    return opcao


#Lê, valida, armazena e retorna o nome
def ler_nome():
    while True:
        nome = input("Digite o nome do aluno: ")
        if len(nome) < 2:
            print("O nome deve ter ao menos dois caracteres.")
        elif not nome.isalpha():
            print("O nome não pode conter caracteres especiais ou números.")
        else:
            return nome


#Lê, valida, armazena e retorna a lista de notas
def ler_notas():
    notas = []
    counter = 0
    #string para personalizar as mensagens para o utilizador
    strings = ["primeira", "segunda", "terceira", "quarta", "quinta", "sexta", "sétima", "oitava", "nona", "décima",
        "décima primeira", "décima segunda", "décima terceira", "décima quarta", "décima quinta", "décima sexta",
        "décima sétima", "décima oitava", "décima nona", "vigésima"]
    try:
        limite = int(input("Quantas notas deseja registar? (Min. 5) \n->"))
        while True:
            if limite == counter:
                break
            if limite < 5:
                limpar_terminal()
                print("Devem ser inseridas no mínimo 5 notas, tente novamente.\n")
                return ler_notas()
            else:
                try:
                    print("Digite a",strings[counter],"nota (entre 0 e 20):")
                    nota = float(input("->"))
                    if 0 <= nota <= 20:
                        notas.append(nota)
                        counter += 1
                    else:
                        print("Nota inválida!")
                except:
                    print("Entrada de caracteres inválidos deve inserir um número entre 0 e 20.")
    except:
        limpar_terminal()
        print("Entrada de caracteres inválidos deve inserir um número, igual ou maior que 5.")
        return ler_notas()
    limpar_terminal()
    return notas


#Exibe a lista de nomes
def mostrar_nomes(nomes):
    limpar_terminal()
    print("Nomes dos alunos:")
    for indice, nome in enumerate(nomes):
        print("Aluno(a) {}: {}".format(indice+1,nome))


#Exibe a lista de nomes e as notas
def mostrar_nomes_notas(nomes, notas):
    limpar_terminal()
    print("Nomes e notas:")
    for i in range(len(nomes)):
        print(f"{nomes[i]}, {notas[i]}")


#Elimina um aluno e as notas relacionadas a este aluno
def eliminar_aluno(nomes, notas,media):
    limpar_terminal()
    nome_eliminar = input("Digite o nome do aluno a ser eliminado: ")
    if nome_eliminar in nomes:
        indice = nomes.index(nome_eliminar)
        if not media:
            del nomes[indice]
            del notas[indice]
            print("Aluno eliminado com sucesso!")
        else:
            del nomes[indice]
            del notas[indice]
            del media[indice]
            print("Aluno eliminado com sucesso!")
        return True
    else:
        print("Aluno não encontrado!")
        return False


#Soma as notas por aluno
def calcular_soma(nomes, notas):
    limpar_terminal()
    print("Alunos, notas e soma das notas: ")
    for i in range(len(nomes)):
        nome = nomes[i]
        soma_notas = sum(notas[i])
        print(f"Aluno: {nome}, Notas: {notas[i]} - Total: {soma_notas}")


# Encontra e exibe a maior nota por aluno e a maior nota entre todos os alunos
def encontrar_maior(nomes, notas):
    limpar_terminal()
    if not notas:
        print("Não há alunos registrados.")
        return
    
    maiores_notas = [max(nota) for nota in notas]
    maior_nota_total = max(maiores_notas)
    indices_maiores_alunos = [i for i, nota in enumerate(maiores_notas) if nota == maior_nota_total]
    print("A maior nota total é: {:.2f}\n".format(maior_nota_total))
    
    print("Maior nota por aluno:")
    for i in range(len(nomes)):
        nome = nomes[i]
        nota = max(notas[i])
        print(f"Aluno: {nome}, Nota: {nota}")
    
    if len(indices_maiores_alunos) == 1:
        indice_maior_aluno = indices_maiores_alunos[0]
        print(f"\nAluno com a maior nota: {nomes[indice_maior_aluno]} - Nota: {maior_nota_total:.2f}")
    else:
        print("\nAlunos com a maior nota:")
        for indice in indices_maiores_alunos:
            print(f"- Aluno: {nomes[indice]} - Nota: {maior_nota_total:.2f}")


# Encontra a menor nota por aluno e a menor nota entre todos os alunos, mesma lógica do código anterior porém para min.
def encontrar_menor(nomes, notas):
    limpar_terminal()
    if not notas:
        print("Não há alunos registrados.")
        return
    
    menores_notas = [min(nota) for nota in notas]
    menor_nota_total = min(menores_notas)
    indices_menores_alunos = [i for i, nota in enumerate(menores_notas) if nota == menor_nota_total]
    print("A menor nota total é: {:.2f}\n".format(menor_nota_total))
    
    print("Menor nota por aluno:")
    for i in range(len(nomes)):
        nome = nomes[i]
        nota = min(notas[i])
        print(f"Aluno: {nome}, Nota: {nota}")
    
    if len(indices_menores_alunos) == 1:
        indice_menor_aluno = indices_menores_alunos[0]
        print(f"\nAluno com a menor nota: {nomes[indice_menor_aluno]} - Nota: {menor_nota_total}")
    else:
        print("\nAlunos com a menor nota:")
        for indice in indices_menores_alunos:
            print(f"- Aluno: {nomes[indice]} - Nota: {menor_nota_total}")



#Calcula a média de cada aluno e a média geral
def calcular_media(nomes, notas, medias,dados_atualizados):
    limpar_terminal()
    print("Média dos alunos: ") 
    medias_por_aluno = []
    for i in range(len(nomes)):
        nome = nomes[i]
        soma_notas = sum(notas[i])
        media_aluno = soma_notas / len(notas[i])
        medias_por_aluno.append(media_aluno)
        print(f"Aluno: {nome}, Notas: {notas[i]} - Média: {media_aluno}")
    media_geral = media_geral = sum(medias_por_aluno) / len(medias_por_aluno)
    medias = medias_por_aluno
    dados_atualizados = False
    return medias, media_geral, dados_atualizados


#Conta a quantidade de alunos que estão acima da média e a seguir exibe os nomes e as médias
def contar_acima_media(nomes, medias, media_geral,dados_atualizados):
    limpar_terminal()
    if (media_geral == None):
        print("Antes de verificar os alunos que estão acima da média geral, por favor calcule a média (op 7)")
    else:
        if (dados_atualizados):
            print("Um ou mais alunos foram removidos, É necessário recalcular a média.")
            return 
        else:
            acima_media = sum(1 for media in medias if media > media_geral)
            print(f"Número de alunos acima da média geral: {acima_media}")
            if(acima_media > 0):
                print("Alunos acima da media geral ({}):".format(media_geral))
                for index,media in enumerate(medias):
                    if(media > media_geral):
                        print("O Aluno: {}, obteve a média: {:.2f}, ficando acima da média geral: {:.2f}".format(nomes[index], media, media_geral))
            else:
                print("Nenhum aluno ficou acima da média geral")
            

#Conta a quantidade de alunos que estão abaixo da média e a seguir exibe os nomes e as médias
def contar_abaixo_9_5(nomes, medias):
    limpar_terminal()
    abaixo_9_5 = 0
    if not medias:
        print("Antes de verificar os reprovados, por favor calcule a média (op 7)")
        return
    else:
        abaixo_9_5 = sum(1 for media in medias if media < 9.5)
        if (abaixo_9_5 > 0):
            print(f"Número de alunos com notas abaixo de 9.5: {abaixo_9_5}")
            print("Alunos abaixo da nota de corte (9.5):")
            for index,media in enumerate(medias):
                if(media < 9.5):
                    print("Aluno: {}, média: {:.2f}".format(nomes[index], media))
        else:
                print("Nenhum aluno ficou abaixo da nota de corte 9.5")


#Verifica se a lista de alunos está vazia e encerra a aplicação
def verificar_lista(nomes):
    if(len(nomes) == 0):
        limpar_terminal()
        print("A lista de alunos está vazia, reinicie a aplicação...")
        return True


#Pausa o sistema e aguarda uma entrada do utilizador
def pausar():
    os.system('pause')


#Limpa as informações no ecrã
def limpar_terminal():
    os.system('cls')

#função principal    
def main():
    #listas principais
    nomes = []
    notas = []
    medias = []
    
    media_geral = None #media geral
    aluno_removido = False #variavel de controle
    
    introducao()
    pausar()
    limpar_terminal()
    registar_aluno_notas(nomes,notas)
    while True:
        resposta = input("Deseja inserir novo aluno e suas notas (s/n)? ").lower()
        match resposta:
            case "n":
                break
            case "s":
                registar_aluno_notas(nomes,notas)
            case _:
                print("Opção inválida! Escolha uma opção válida!\n")

    while True:
        if verificar_lista(nomes): break
        limpar_terminal()
        main_menu()
        opcao = obter_opcao()
        match opcao:
            case 1:
                mostrar_nomes(nomes)
                pausar()
            case 2:
                mostrar_nomes_notas(nomes, notas)
                pausar()
            case 3:
                aluno_removido = eliminar_aluno(nomes, notas,medias)
                pausar()
            case 4:
                calcular_soma(nomes,notas)
                pausar()
            case 5:
                encontrar_maior(nomes, notas)
                pausar()
            case 6:
                encontrar_menor(nomes, notas)
                pausar()
            case 7:
                medias, media_geral, aluno_removido = calcular_media(nomes, notas, medias,aluno_removido)
                print(f"\nMédia geral das notas: {media_geral:.2f}") 
                pausar()
            case 8:
                contar_acima_media(nomes, medias, media_geral,aluno_removido)
                pausar()
            case 9:
                contar_abaixo_9_5(nomes, medias)
                pausar()
            case 10:
                print("Obrigado por utilizar a nossa aplicação, até a próxima!.")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                
if __name__ == "__main__":
    main()