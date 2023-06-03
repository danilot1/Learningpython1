palavra = input('Digite alguma palavra: ')

ocorrencias = ''

i = 0

while i < 10:
    for p in palavra:
        if p == str(i):
            ocorrencias = ocorrencias + str(i) + ' '
    i = i + 1        
print(ocorrencias)

