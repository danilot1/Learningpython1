maior = 0

def maior(x, y):
    if x > y:
        x = maior
        print(maior)
    elif x < y:
        y = maior
        print(maior)
    return x, y 
    
maior(1, 2)

def menor(x, y):
    if x < y:
        x= menor
        print(menor)
    elif y < x:
        y = menor
        print(menor)
    return menor
maior(1,2)

