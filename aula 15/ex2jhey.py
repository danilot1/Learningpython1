def maior(numero1,numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    
def menor(numero1, numero2):
    if numero1 < numero2:
        return numero1
    else:
        return numero2
    
def media(numero1, numero2):
    return(numero1 + numero2)/2

num1 = int(input())
num2 = int(input())

print('O maior', maior(num1,num2))
print('O menor', menor(num1,num2))
print('Media', media(num1,num2))