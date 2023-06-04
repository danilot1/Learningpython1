number = int(input())
contador = 0
for i in range (1, number* 4 + 1, 1):
    if i % 4 == 0:
        print('PUM')
    else:
        print(i, end=" ")