def somatorio():
    contador = 0
    numero = int(input())
    for i in range(1, numero+1):
        contador = contador + i
    print(contador)
    return numero,contador
somatorio()