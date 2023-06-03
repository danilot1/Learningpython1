user_1 = 'fulano'
user_2 = 'ciclano'
user_3 = 'beltrano'
senha1 = 'carro'
senha2 = 'bola'
senha3 = 'pipa'
usuario = input('Digite o seu nome de usuario ')
if usuario == user_1:
    senha_de_acesso = input('digite sua senha: ')
    if senha_de_acesso == senha1:
        print('Login Realizado com sucesso')
    else:
        print('Acesso negado')
elif usuario == user_2:
    senha_de_acesso = input('digite sua senha: ')
    if senha_de_acesso == senha2:
        print('Login Realizado com sucesso')
    else:
        print('Acesso negado')
elif usuario == user_3:
    senha_de_acesso = input('digite sua senha: ')
    if senha_de_acesso == senha3:
        print('Login Realizado com sucesso')
    else:
        print('Acesso negado')        
else:
    print('Erro, acabou o programa') 