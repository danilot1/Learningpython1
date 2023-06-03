def fatorial(numero):
    if numero == 0:
        return 1
    else:
        resposta = 1
        while numero >= 1:
            resposta = resposta * numero
            numero = numero - 1
        return resposta
numero = int(input('Digite o numero do fatorial: '))
fat = fatorial(numero)
print(fat)