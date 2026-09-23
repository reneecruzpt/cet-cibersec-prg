import os

path = os.getcwd()

print(path)

#new_path = ''
#os.chdir(new_path)

files = os.listdir(path)

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
        
extension = '.' + input('Qual a extensão dos ficheiros pretende visualizar?')

for file in files:
    if file.endswith(file):
        print(file)

