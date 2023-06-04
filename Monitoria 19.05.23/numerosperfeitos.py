numero1 = int(input())
numero2 = int(input())
soma_divisores = 0
for i in range(numero1,numero2+1):
    soma_divisores = 0
    for j in range(1,i):
        if i % j == 0:
            soma_divisores += j
    if soma_divisores == i:
        print(i)
