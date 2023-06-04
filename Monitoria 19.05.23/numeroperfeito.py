number =int(input())
soma_divisores = 0

for i in range(1,number):
    if i <= number/2:
        if number % i == 0:
            soma_divisores += i

if soma_divisores == number:
    print('É perfeito')
else:
    print('Não é perfeito')
