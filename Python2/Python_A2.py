'''
Atividade Python 2 
Strings
Dev: Reneê Cruz, 21/02/2024
'''

print("1 - Nome invertido e com maiúsculas:")
name = input("Insira seu nome\n->")
print(name[::-1].upper())

print("2 - Nome em escada crescente:")
for element in range(len(name)):
    print(name[:element+1].upper())
    
print("3 - Nome em escada decrescente:")
for element in range(len(name),0,-1): #começa no tamanho do nome vai até zero com decremento de -1
    print(name[:element].upper())
    
grades = []
for element in range(10):
    grade = input(f"Insira a nota {element+1}\n->")
    grades.append(grade)
    

#1. Lista introduzida - Mostra os elementos da lista introduzida, formato de lista;
print(f"Elementos da lista {grades}")
print(f"Formato da lista {type(grades)}\n")

#2. Elementos da Lista - Mostra todos os elementos na ordem em que foram introduzidos, todos na mesma linha, um ao
#lado do outro com um espaço entre eles, sem ser formato de lista (ex: 12.3 3.5 11.0 15.9);
grades_str = ""
for element in grades:
    grades_str += element + " "
    
print(f"Lista em string com elementos separados por espaços: {grades_str}\n")

# 3. Ordem Inversa - Mostra todos os elementos na ordem inversa à que foram introduzidos, na vertical;

print("Ordem inversa dos elementos na vertical:")
for grade in reversed(grades):
    print(grade)
    
# 4. Ordem crescente - Mostra todos os elementos em ordem crescente, na mesma linha;
asc_grades = sorted(grades, key=float)
grades_str_asc = " ".join(asc_grades)
print(f"\nElementos em ordem crescente: {grades_str_asc} \n")

# 5. Soma dos elementos - Calcula e mostra a soma dos elementos;
total = 0
for grade in grades:
    total += float(grade)
print(f"O valor total da soma é: {total}\n")

# 6. O maior elemento – Calcula o maior elemento e mostra;
max = 0
for grade in grades:
    if float(grade) > max:
        max = float(grade)
print(f"O maior valor é: {max}\n")

# 7. O menor elemento – Calcula o menor elemento e mostra;
min = 1000
for grade in grades:
    if float(grade) < min:
        min = float(grade)
print(f"O menor valor é: {min}\n")

# 8. Média dos elementos - Calcula e mostra a média dos elementos;
total = 0
for grade in grades:
    total += float(grade)
avg = total / len(grades)
print(f"O valor da média é: {avg}\n")

# 9. Acima da média - Mostra quantos e quais são os elementos acima da média calculada;
count = 0
for grade in grades:
    if float(grade) > avg:
        print(f"A nota {float(grade)} está acima da média {avg}")
        count += 1
print(f"O total de notas acima da média é de: {count}\n")

# 10. Elementos negativos (menores que 9,5) - Mostra a quantos e quais são os elementos abaixo de 9.5;
count = 0
for grade in grades:
    if float(grade) < 9.5:
        print(f"A nota {float(grade)} está abaixo da nota de corte 9.5 ")
        count += 1
print(f"O total de notas abaixo da nota de corte é de: {count}\n")