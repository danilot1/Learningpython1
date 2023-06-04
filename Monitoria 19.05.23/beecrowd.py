senha = int(input())
senha_correta = 2002
while senha != senha_correta:
    senha = int(input())
    print('Senha Invalida')
    if senha == senha_correta:
        print('Acesso Permitido')