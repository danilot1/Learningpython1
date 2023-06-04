N = int(input())
contadorin = 0
contadorout = 0
for i in range(N):
    Number = int(input())
    if Number >= 10 and Number <= 20:
        contadorin = contadorin + 1
    else:
        contadorout = contadorout + 1
print(contadorin,'in')
print(contadorout,'out')
    