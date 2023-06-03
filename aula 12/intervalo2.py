N = int(input())
contadorin = 0
contadorout = 0
for i in range(N):
    N = int(input())
    if N >= 10 and N <= 20:
        contadorin = contadorin+1
        print(contadorin,'in')
    else:
        contadorout = contadorout+1
        print(contadorout,'out')