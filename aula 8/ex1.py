nome = input('Digite seu nome ')
tamanho = len(nome)
if tamanho < 3 or tamanho > 12:
    print('invalido')
else:
    print('Válido')