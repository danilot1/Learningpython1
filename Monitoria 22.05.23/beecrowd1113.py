x, y  = map(int,input().split())  

if x > y:
    temp = x
    x = y
    y = temp

while x != y:
    if x > y :
        print('Decrescente')
    elif y > x:
        print('Crescente')
    elif x == y:
        break
    x, y  = map(int,input().split())  