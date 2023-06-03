def somatorio(numero):
    i = 0
    soma = 0
    while i <= numero:
        soma = soma +i 
        i = i + 1
    return soma

numero = int(input('Digite um numero '))
s = somatorio(numero)
print(s)