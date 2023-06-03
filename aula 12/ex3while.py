numero1 = int(input())
numero2 = int(input())
maior = 0
menor = 0
soma = 0 
quantidade = 0

if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1
    
while i <= maior:
    soma = soma + i
    quantidade = quantidade + 1
    i = i + 1
print(soma/quantidade)