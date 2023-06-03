user_1 = 'fulano'
user_2 = 'ciclano'
senha = 'carro'

usuario = input('Digite o seu nome de usuario ')
if usuario == user_1 or usuario == user_2:
    senha_de_acesso = input('digite sua senha: ')
    if senha_de_acesso == senha:
        print("Acesso liberado")
    else:
        print('Acesso negado')
else:
    print('Erro, acabou o programa') 