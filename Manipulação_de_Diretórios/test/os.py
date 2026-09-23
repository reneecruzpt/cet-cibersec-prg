import os

path = os.getcwd()
print("Nome do sistema operativo: " + os.name)
environ_map = os.environ
#print(environ_map)
print(environ_map['HOMEPATH'])

print(path)
files = os.listdir(path)
print(files)

new_path = r'C:\Users\Renee Cruz\Documents\another_folder' #r permite o uso da \
os.chdir(new_path)

print(new_path)
files = os.listdir(new_path)

print("\nDiretórios em {}".format(new_path))
for dir in files:
    if os.path.isdir(dir):
        print(dir)

print("\nFicheiros em {}".format(new_path))        
for file in enumerate(files):
    if os.path.isfile(file):
        print(file)

#imprimir lista
#os.listdir(path)

# for extension in files:
#     if extension.endswith('.py'):
#         print(extension)

# for dir in files:
#     if os.path.isdir(dir):
#         print(dir)
        
# for file in files:
#     if os.path.isfile(file):
#         print(file)
        
# extension = '.' + input('Qual a extensão dos ficheiros pretende visualizar?')

# for file in files:
#     if file.endswith(extension):
#         print(file)


'''
# new_path = r'C:\Users\Renee Cruz\Documents\another_folder' #r permite o uso do backslash (\) sem causar problemas 
# os.chdir(new_path) #troca o diretório para o indicado no novo path

# print('Novo diretório de trabalho' , os.getcwd()) #exibe o diretório

# print('Este diretorio tem os seguintes ficheiros: ') 

# for f in os.listdir(): #lista ficheiros e pastas
#     print(f)
    
#os.startfile('restricted_dir') #abre um diretório no S.O.

# print('Os ficheiros da pasta são:')
# for f in os.listdir():
#     print(f)

# folder = input('\nQual o diretorio pretende abrir?\n ->')
# try:
#     os.startfile(folder)
# except:
#     print("A pasta não existe")


# print('Os ficheiros do diretório {} são : '.format(folder))
# for f in os.listdir(f'{new_path}\{folder}'):
#     print(f)

# novo_caminho = f'{new_path}\{folder}'
# os.chdir(novo_caminho)
# print(os.getcwd())


# filename = input("Qual ficheiro deseja eliminar?\n->")
# os.remove(filename + '.txt') #elimina ficheiros

# dirname = input("Qual diretório deseja eliminar?\n->")
# try:
#     os.rmdir(dirname) #apaga diretórios vazios
# except:
#     confirmation = input("O diretório não está vazio, deseja eliminar mesmo assim? (s/n)\n->").lower()
#     if confirmation == 's': shutil.rmtree(dirname) #elimina diretórios vazios ou não

# while(True):    
#     dirname = input("Insira o nome do diretório que deseja eliminar os ficheiros?\n->")
#     try:
#         os.chdir(f'{new_path}\{dirname}')
#     except:
#         print("Diretório não localizado ou inexistente")
#     fileList = os.listdir()
#     for i in fileList: print(i)

#     check = input("Deseja eliminar os ficheiros? (s/n)\n->").lower()
#     if check == 's':
#         for file in fileList:
#             if os.path.isfile(file): ###??
#                 os.remove(file)
#     else:
#         print("Operação cancelada")

#listDir(path)
# path = pathPreviousFolder(os.getcwd())
# printPath(path)
# #listDir(path)
# path = pathPreviousFolder(os.getcwd())
# printPath(path)
# path = pathPreviousFolder(os.getcwd())
# printPath(path)
# path = pathPreviousFolder(os.getcwd())
# printPath(path)

# path = previousFolder(os.getcwd())
# printPath(path)

#dirname = input("Qual diretório deseja eliminar?\n->")
#os.rmdir(dirname) #apaga diretórios vazios
#shutil.rmtree(dirname) #elimina diretórios vazios ou não
pass
'''