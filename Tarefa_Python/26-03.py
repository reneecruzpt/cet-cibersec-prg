def verificar(string):
    lista = string.split(' ')
    if len(lista) > 2:
        print("A string possui mais de duas palavras")
    else:
        substring1 = lista[0]
        substring2 = lista[1]
        if substring1[0] == substring2[0]:
            print("As duas palavras {} e {} começam com o mesmo caractere {}\n".format(lista[0], lista[1],substring1[0]))
        else:
            print("As duas palavras não começam com o mesmo caractere\n")


while True:
    string = input("Insira duas palavras separadas por um espaço\n->")
    verificar(string)