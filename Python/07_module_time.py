import time

# print(time)

# print(dir(time))

# for item in dir(time):
#     print(item)


print(time.localtime())
#hora atual
tempo = time.localtime()
hora = time.strftime("%H:%M:%S", tempo)
print('Hora atual:',hora)

#data e hora atual
data_hora =  time.ctime()
print('Data e Hora atual:',data_hora)

for item in data_hora:
    print(item)

dia_da_semana = data_hora[0:3]
print(dia_da_semana)

mes = data_hora[4:8]
print(mes)

dia = data_hora[8:10]
print(dia)

hora = data_hora[11:19]
print(hora)

ano = data_hora[20:24]
print(ano)

#desenvolvendo um cronometro
def cronometro():
    input("Pressione Enter para iniciar o cronômetro...")
    start = time.time()  # Captura o tempo de início
    input("Pressione Enter para parar o cronômetro...")
    end = time.time()  # Captura o tempo de término

    elapsed_time = end - start  # Calcula o tempo decorrido
    print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
cronometro()

#desenvolvendo um temporizador
def temporizador(segundos):
    for i in range(segundos, 0, -1):
        print(f'Tempo restante: {i} segundos', end='\r')
        time.sleep(1)
    print('Tempo esgotado!                             ')  # Espaços extras para sobrescrever a linha anterior

# Solicita o tempo em segundos do usuário
tempo = int(input("Digite o tempo do temporizador em segundos: "))
temporizador(tempo)

while True:
    print('Olá')
    time.sleep(5)
    print('Tudo bem?')

