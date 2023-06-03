palavra = input()
contador = 0
tamanho = len(palavra)

i = 0

while i < tamanho:
    if palavra[i] == 'a':
        contador = contador + 1
    i = i + 1
print(contador)