numero1 = int(input())
numero2 = int(input())
if numero1 % 2 == 0:
    numero1 = numero1 + 1
for n in range (numero1 , numero2, 2):
    print(n)
#for n in range (numero1 , numero2 + 1, 2):
#    print(n)