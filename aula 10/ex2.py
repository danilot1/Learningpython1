numero1 = int(input())
numero2 = int(input())

maior = 0
menor = 0

if numero1 < numero2:
    numero1 = menor
    numero2 = maior
else:
    numero1 = maior
    numero2 = menor

while menor <= maior:
    if menor %2 == 0:
        if menor % 6 ==0:
            menor = menor + 1
            continue
        print(menor)
        menor = menor + 1
    print(menor)
    menor = menor + 1
