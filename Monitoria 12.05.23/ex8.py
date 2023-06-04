X = int(input())
Y = int(input())
contador = 0
if X > Y:
    temp = X
    X = Y
    Y = temp
for i in range(X, Y):
    if not i % 2 == 0:
        contador = contador + i
print(contador)