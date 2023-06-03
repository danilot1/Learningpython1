numero1 = int(input())
numero2 = int(input())


if numero1 < numero2:
    contador = 0
    contador = numero1
    for numero1 in range(contador,numero2 + 1):
        print(numero1)
elif numero2 < numero1:
    contador = 0
    contador = numero2
    for numero2 in range(contador,numero1 + 1):
        print(numero2)
        