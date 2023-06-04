nome = "joao da silva"  #nome do usuário
numero1 = 15
numero2 = 20

nome = 'maria dos santos'
presenca = True
peso = 74.3
dormir = False
falso = False
verdadeiro = True

cpf = 12345678901  #trabalhar cpf como string
cpf = '01234567890'
cpf = '012.345.789-10'

numero1 = '10'  #string
numero2 = '15'  #string
numero3 = 10  #int
numero4 = 15  #int

print(numero1 + numero2)
print(numero3 + numero4)

nomeaula100323 = input('Digite seu nome: ')
print('ola, meu nome e:', nomeaula100323)

numero5 = int(input('Digite seu numero: '))
numero6 = int(input('Digite seu segundo numero: '))

print('Divisão normal:', numero5 / numero6)
print('Divisão inteira', numero5 // numero6, ',e sobra: ', numero5 % numero6)

#Operação de raiz quadrada
numero7 = int(input('Digite um numero para extrair a raiz quadrada'))
print(numero7**(1 / 2))
numero8 = int(input('Digite um numero para extrair a raiz cúbica'))
print(numero8**(1 / 3))

numero9 = int(input('Digite um número: '))  #usando operador de atribuição!!!!
numero10 = int(
  input('Digite outro numero: '))  #continuo usando operador de atribuição!!!

print(numero9 == numero10)  #estou comparando os números!!!
print('True - são iguais')
print('False - são diferentes')
print(numero9, numero10)

#nome1 = input("Qual o seu nome ? ")
#print("Bem vindo", nome1)
#idade = int(input("Qual a sua idade ? "))
#if idade>=18:
#print ("Cuidado voce já poder cumprir pena")
#else:
#print("Tá tranquilo pode aproveitar a vida com muita ética, juizo e seriedade")
#def(soma):

#Outra forma de exibir a saída de dados
x = float(input('Digite um numero: '))
x = x / 3

print("Um terco do numero digitado é:{:.4f}".format(x))

dividendo = 8
divisor = 2
quociente = dividendo / divisor
print(quociente)