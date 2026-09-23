# Cet Cibersegurança - Formador Paulo Rodrigues 
#
# Operações com o módulo OS (Operating System)
# App Gestão de ficheiros e diretórios
# Reneê Cruz, 01/04/2024


import os #operating system dependencies

import shutil #High-level file operations

def printPath():
    print(f"O Path atual é: {os.getcwd()}")


def previousFolder():
    path = os.getcwd()
    pathManagement = path.split("\\")
    resultPath = ''
    for i in pathManagement[:-1]:
        resultPath += i + "\\"
        os.chdir(resultPath)
    print("Path antigo: {}".format(path))
    printPath()


def navigate():
    path = os.getcwd()
    print("Lista de diretórios disponiveis:")
    listPart('folder')
    folder = input("\nEscreva o nome do diretório desejado:\n->")
    pathManagement = path.split("\\")
    resultPath = ''
    for i in pathManagement:
        resultPath += i + "\\"
    os.chdir(resultPath + folder)
    print("Path antigo: {}".format(path))
    printPath()


def freeNavigation():
    path = input("Escreva o path desejado:\n->")
    try:
        os.chdir(path)
        print("Path atualizado")
        printPath()
    except:
        print("O path {}, não é um path válido.".format(path))


def getItems():
    path = os.getcwd()
    items = os.listdir(path)
    return items


def printItems():
    print("Diretórios e ficheiros disponiveis:")
    list = getItems()
    print('\n'.join(each for each in list))


def listPart(string):
    path = os.getcwd()
    items = os.listdir(path)
    resultList = []
    if string == 'file':
        for element in items:
            if os.path.isfile(element):
                resultList.append(element)
    elif string == 'folder':
        for element in items:
            if os.path.isdir(element):
                resultList.append(element)
    print('\n'.join(str(item) for item in resultList))


def enumeratedList(string):
    path = os.getcwd()
    dir = os.listdir(path)
    enumList = []
    counter = 0
    if string == 'file':
        for element in dir:
            if os.path.isfile(element):
                counter += 1
                print(counter , '-', element)
                enumList.append(element)
    elif string == 'folder':   
        for element in dir:
            if os.path.isdir(element):
                counter += 1
                print(counter , '-', element)
                enumList.append(element)        
    return enumList


def removeFile():
    list = enumeratedList('file')
    op = None
    while type(op) != int:
        try:
            op = int(input("Qual ficheiro deseja remover? 0 = sair. \n->"))
            if op == 0: menu()
        except:
            print("Entrada inválida!")
    try:        
        check = input("Tem certeza que deseja remover o ficheiro {} (s/n)?".format(list[op-1]))
    except:
        print("O valor informado não consta na lista.")
        return menu()
    if check == 's': 
        os.remove(list[op-1])
        print("Ficheiro removido")
    else: print("Operação cancelada")


def removeByExtension():
    list = getItems()
    exists = False
    ext = "." + input("Qual extensão deseja remover? (sem o \".\") 0 = sair. \n->")
    
    for i in list:
        if i.endswith(ext):
            print(i)
        exists = True


    if exists == True:
        check = input("Confirme para eliminar todos os ficheiros. ATENÇÃO está ação é irreversível! (s/n)").lower()        
        if check == 's':
            for i in list:
                if i.endswith(ext):
                    os.remove(i)
            print("Ficheiros eliminados.")
    else:
        print("Não foram encontrados ficheiros com a extensão {} .".format(ext))


def removeFolder():
    list  = enumeratedList('folder')
    op = None
    while type(op) != int:
        try:
            op = int(input("Qual diretório deseja remover? 0 = sair. \n->"))
            if op == 0: menu()
        except:
            print("Entrada inválida!")  
    try:        
        check = input("Tem certeza que deseja remover o diretório {} (s/n)?".format(list[op-1]))
    except:
        print("O valor informado não consta na lista.")
        return menu()
    if check == 's':
        try:
            os.rmdir(list[op-1])  
            print("Ficheiro removido")
        except:
            confirmation = input("O diretório não está vazio, deseja eliminar mesmo assim? (s/n)\n->").lower()
            if confirmation == 's': shutil.rmtree(list[op-1])
    else: print("Operação cancelada")

def getName(string):
    invalidChars = '<>:"/\|?*'
    text = 'ficheiro' if string == 'file' else 'diretorio'
    name = input("Escreva o nome do {}\n->".format(text))
    if len(name) > 50:
        print("O nome da pasta é demasiado grande")
        return getName()
    for char in name:
        if char in invalidChars:
            print("Caracteres como {}, não são aceitos.".format(invalidChars))
            return getName()
    return name


def createFolder():
    folderName = getName('folder')
    try:
        os.mkdir(folderName)
    except:
        print("Ocorreu um erro, tente novamente.")


def rename():
    list = enumeratedList('file')
    try:
        op = int(input("Qual ficheiro deseja renomear?\n->"))
        if op > len(list):
            print("O número informado não consta na lista")
        else:
            holdExtension = list[op-1].split(".")
            newname = getName('file') + "." + holdExtension[-1]
            check = input("Confirma a alteração de \"{}\" por \" {}\" (s/n)?".format(list[op-1],newname)).lower()
            if check == 's':
                os.rename(list[op-1],newname)
                print("Operação realizada com sucesso")
            else:
                print("Operação cancelada")
    except:
        print("Insira um número inteiro")


def menu():
    os.system('cls')
    op = subop = None
    op = input("Escolha uma opção:\na - Path atual\nb - Recuar diretório\nc - Criar diretório\nd - Remover\nl - Listar\nn - Navegação\nr - Renomear\nx - Encerrar\n->")
    match op:
        case 'x':
            return False
        case 'a':
            printPath()
        case 'b' :
            previousFolder()
        case 'c' :
            createFolder()
        case 'd':
            os.system('cls')
            subop = input("O que deseja remover?\n1 - Ficheiro\n2 - Diretório\n3 - Ext\n->")
            match subop:
                case '1':
                    removeFile()
                case '2':
                    removeFolder()
                case '3':
                    removeByExtension()
                case _:
                    print("Opção inválida")
        case 'l':
            os.system('cls')
            subop = input("O que deseja listar?\n1 - Lista completa\n2 - Ficheiros\n3 - Diretórios\n->")
            match subop:
                case '1':
                    printItems()
                case '2':
                    listPart('file')
                case '3':
                    listPart('folder')
                case _:
                    print("Opção inválida")
        case 'n':
            os.system('cls')
            subop = input("Navegação\n1 - Guiada\n2 - Livre\n0 - Sair\n->")
            match subop:
                case '0':
                    menu()
                case '1':
                    navigate()
                case '2':
                    freeNavigation()
                case _:
                    print("Opção inválida")
        case 'r':
            rename()
        case _:
            print("Opção inválida")
    os.system('pause')
    return True

isRunning = True    
while isRunning:
    isRunning = menu()