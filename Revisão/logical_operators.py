#Na lógica, eles são chamados de conectivos lógicos.

#Serve, para verificar se uma ou mais condições são verdadeiras ou não, são eles:

#and - Retorna True APENAS quando ambas as condições são verdadeiras, em todas as outras situações retorna False.
#or - Retorna True quando uma das condições ou ambas as condições são verdadeiras, retorna False APENAS quando ambas as condições são falsas.
#not - Negação, inverte a lógica da verificação padrão, exemplo not False é equivalente a True

#bool - True or False
verdadeiro = True
falso = False

#verificação do and, o E lógico
# print(verdadeiro and falso) # True and False = False
# print(verdadeiro and verdadeiro) #True and True = True
# print(2 > 1 and 5 > 2) #True

#verificação do or, o OU lógico
# print(verdadeiro or falso) #True or False = True
# print(verdadeiro or verdadeiro) #True or True = True
# print(falso or falso)#False or False = False

#verificação do not
# print(not verdadeiro) #False
# print(not falso) #True

#not com and
# print(not verdadeiro and falso) #False and #False = False
# print(not verdadeiro and not falso) #False and True = False
# print(verdadeiro and not falso) #True and True = True

#not com or
# print(not verdadeiro or falso) #False or False = False
# print(not verdadeiro or not falso) #False or True = True
# print(verdadeiro or not falso) #True or True = True

#Utilização do and e or em uma mini aplicação - Descubra o número par

# print("Verificação de Pares") #Mensagem informativa para o utilizador

# var1 = int(input("Entre o primeiro número:\n-> "))

# var2 = int(input("Entre o segundo número:\n-> "))

# if var1 % 2 == 0 and var2 % 2 == 0: #se ambas as condições forem verdadeiras, ou seja se ambos os números divididos por dois tiverem resto zero, ambos são números pares
#     print("Ambos os números são pares")
# elif var1 % 2 == 0 or var2 % 2 == 0: #Se a verificação do resto da divisão de var1 por 2 for igual a 0 OU o resto da divisão de var2 por 2 for igual a 0
#     print("Um dos dois números é par")
# else: #Se o resto da divisão de ambos os números for diferente de 0:
#     print("Nenhum dos números inseridos é par")

#utilizando o not

# print("Verificação de Pares") #Mensagem informativa para o utilizador

# var1 = int(input("Entre o primeiro número:\n-> "))

# var2 = int(input("Entre o segundo número:\n-> "))

# if not var1 % 2 == 0 and not var2 % 2 == 0: # o resultado de var1 % 2 == 0 não é 0 e o resutado de var2 % 2 == 0 também não é zero -> True (Ambos Ímpares)
#     print("Nenhum dos números inseridos é par")
# elif not var1 % 2 == 0 or not var2 % 2 == 0: #se o resultado de um deles não for igual a zero -> True (Um deles é ímpar)
#     print("Um dos dois números é par")
# else: #ambos os resultados são iguais a zero, então ambos são pares.
#     print("Ambos os números são pares")

