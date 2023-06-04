M, N  = map(int,input().split())   
while not (M <= 0 or N <= 0):
    contador = 0
    if M > N:
        temp = M
        M = N
        N = temp
    for i in range(M, N+1):
        contador = contador + i
        print( i, end =" ")
    print(f'Sum={contador}')
    M, N  = map(int,input().split())   
    