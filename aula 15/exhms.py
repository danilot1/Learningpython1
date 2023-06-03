def tempo(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    time = str(horas) + ':' + str(minutos) + ':' + str(segundos)
    return time

temp = int(input("Digite a quantidade de segundos "))

print(tempo(temp))