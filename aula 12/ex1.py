numero1 = int(input())
numero2 = int(input())
contador = 0

if numero1 > numero2:
    temp = numero1
    numero1 = numero2
    numero2 = temp

    
for i in range (numero1, numero2+1):
    contador = contador + i
print(contador)