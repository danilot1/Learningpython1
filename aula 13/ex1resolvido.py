numero = int(input())

i = 1
j = 1 

impressao = ''

while i <= numero:
    while j <= i:
        impressao = impressao + str(j) + ' '
        j += 1
    
    print(impressao)
    impressao = ''
    j = 1
    i = i + 1

print('codigo finalizado')