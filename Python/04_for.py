#o ciclo for é utilizado quando sabemos a quantidade de iterações que queremos fazer
n = 5
for iteracao in range(n): #os índices iniciam em zero, o loop será executado de 0 até n-1
    print(iteracao)
#print()

nome = 'maria'

for letra in nome:
    print(letra)
#print()

for letra in nome:
    print(letra,end='')
#print()

for letra in nome:
    print(letra,end='@')
print() 

lista = ['m','a','r','i','a']
print(lista)

for letra in lista:
    print(letra,end='')
print()   
 
#descobrindo se existe um símbolo proíbido em uma palavra
palavra = input('entre uma palavra:\n->')
proibido = '@'

for letra in palavra:
    if letra == proibido:
        print('A palavra contem um símbolo proibido')
        palavra = ''
        break

if palavra != '':
    print('A palavra foi aceite')