numero = int(input('Digite o seu numero '))
resto = numero%2
if resto != 0 and numero > 30 and numero <50:
    print('Acertou')
else:
    print('Errou')