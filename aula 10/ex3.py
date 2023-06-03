numero = float(input('digite seu numero'))
soma = 0
quantidade = 0

while numero >= 0:
    soma = soma + numero
    quantidade = quantidade + 1
    numero = float(input('digite mais um numero'))

media = soma/quantidade
print(media)