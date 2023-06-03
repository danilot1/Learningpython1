numero1 = int(input())
numero2 = int(input())
if numero1 < numero2:
    for x in range(numero1 ,numero2):
        if x %2!=0:
            print(x)
elif numero2 < numero1:
    for x in range(numero2 ,numero1):
        if x %2!=0:
            print(x)
    
#For > while