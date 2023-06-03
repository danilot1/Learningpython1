def maior(numero1,numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    
num1 = int(input())
num2 = int(input())
num3 = int(input())

print ('maior', maior(maior(num1,num2),num3))