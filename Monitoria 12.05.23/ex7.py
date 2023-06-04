numero1 = int(input())
numero2 = int(input())

if numero1 > numero2:
    temp = numero1;
    numero1 = numero2;
    numero2 = temp;
while numero1 <= numero2:
    print(numero1)
    numero1 += 1
   