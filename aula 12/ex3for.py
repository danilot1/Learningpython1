numero1 = int(input())
numero2 = int(input())
soma = 0
contador= 0

if numero1 > numero2:
    temp = numero1
    numero1 = numero2
    numero2 = temp

for i in range (numero1, numero2+1):
    soma = soma + i
    contador = contador + 1
    media = soma/contador
print(media)
