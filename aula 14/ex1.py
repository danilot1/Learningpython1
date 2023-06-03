def teste():
    soma= 1+2
    print(soma)
teste()



def par_ou_impar(numero):
    if numero % 2 == 0:
        print('Par')
    else:
        print('Impar')
par_ou_impar(5)



def numero_perfeito(numero_teste_perfeito):
    soma = 0
    for i in range(1,numero_teste_perfeito):
        if numero_teste_perfeito % i == 0:
            soma = soma + i
    if soma == numero_teste_perfeito:
        print('perfeito')
    else:
        print('Nao e perfeito')
numero_perfeito(28)



def numero_primo(numero_teste_primo):
    i = 2
    primo = True
    while i < numero_teste_primo / 2:
        if numero_teste_primo % i == 0:
            primo = False
            break
        i = i + 1
    if primo:
        print('o numero', numero_teste_primo, 'e primo')
    else:
        print('o numero', numero_teste_primo, 'nao e primo')
numero_primo(7)