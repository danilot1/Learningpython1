N = int(input())

for i in range(N):
    soma = 0
    x, y = map(int,input().split())
    if x > y:
        temp = x
        x = y
        y = temp
    for j in range(x+1,y):
        if not j % 2 == 0:   
            soma = soma + j 
    print(soma)
