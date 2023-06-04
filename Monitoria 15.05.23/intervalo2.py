N = int(input())

for i in range(N):
    N = int(input())
    contadorin = 0
    contadorout = 0
    if N > 10 and N < 20:
        contadorin = contadorin+1
        print(contadorin, 'in')
    if not N > 10 and not N < 20:
        contadorout = contadorout+1
        print(contadorout, 'out')
    