
print("A soma total dos numeros a seguir deve ser no maximo 10")
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
soma_total = num_1 + num_2 + num_1
if soma_total > 10:
    print("O limite foi excedido")
else:
    print("A operacao foi realizada com sucesso")