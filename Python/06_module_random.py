import random

#from random import randint
#print(random.randint(0,1))

#verificando se o número aleatório é par ou ímpar

# num = random.randint(1,10)
# if num%2 == 0:
#     print(num, 'é par\n')
# else:
#     print(num, 'é ímpar\n')

# print('adivinhe o número')
# num = random.randint(0,5)
# print('foi gerado um número entre 0 e 5 (inclusive)')
# while True:
#     guess = int(input('Qual é o número?\n->'))
    
#     if guess == num:
#         print('Parabéns você acertou!',guess,'=',num)
#         break
#     else:
#         print('Você errou! tente novamente')

# print('adivinhe o número')
# num = random.randint(0,5)    
# print('foi gerado um número entre 0 e 5 (inclusive)')   
# chances =  3
# for chance in range(3):
#     guess = int(input('Qual é o número?\n->'))
#     if guess == num:
#         print('Parabéns você acertou!',guess,'=',num)
#         break
#     else:
#         chances -=1
#         print('Você errou! tente novamente chances:',chances,'de 3')
        
#     if chances == 0:
#         print('Fim de jogo, you lose!')

print(random)

print(dir(random))

# for item in dir(random):
#     print(item)