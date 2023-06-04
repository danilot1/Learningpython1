#1. Crie uma aplicação que receba 3 números e divida o primeiro pelo produto do segundo pelo terceiro.
print("Questão 1")
numero1 = 6
numero2 = 2
numero3 = 1

divisao = numero1 / (numero2 * numero3)
print("Resultado", divisao)

print("--------------------------------------------------")

#2 Crie uma aplicação que receba 3 números como entrada, salve o resto da divisão pelos dois primeiros números e verifique se o resultado é maior que o terceiro número digitado.
print("Questão 2")
numero4 = int(input("Digite o primeiro número: "))
numero5 = int(input("Digite o segundo número: "))
numero6 = int(input("Digite o terceiro número: "))

restodadivisao = numero4 % numero5
print("O resto da divisão é maior que o terceiro número digitado ?",restodadivisao > numero6)

print("--------------------------------------------------")
#3 Calcule o delta de uma equação do segundo grau, para isso receba 3 números sendo eles os coeficientes de uma equação de segundo grau(A, B e C).
print("Questão 3")
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

delta = b**2 - 4 * a * c
print("O valor de delta é", delta)
x1 = (-b + (delta**1 / 2) / 2 * a)
x2 = (-b - (delta**1 / 2) / 2 * a)

print("O valor de x1 é", x1)
print("O valor de x2 é", x2)

print("------------------------------------------------")
#4 Crie uma aplicação em que esteja já salvo em uma variável o ano atual e pergunte em que ano o usuário nasceu, então retorne a idade dele(desconsidere os meses e os dias).

print("Questão 4")
ano_atual = 2023
ano_de_nascimento = int(input("Em que ano você nasceu ? "))
idade = ano_atual - ano_de_nascimento
print("Sua idade é:", idade)