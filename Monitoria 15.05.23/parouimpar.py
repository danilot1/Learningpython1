N = int(input())

for i in range(N):
    N = int(input())
    if N % 2 == 0 and N > 0:
       print('EVEN POSITIVE')
    if not N % 2 ==0 and N > 0:
        print('ODD POSITIVE')
    if N % 2 == 0 and N < 0:
       print('EVEN NEGATIVE')
    if not N % 2 ==0 and N < 0:
        print('ODD NEGATIVE')
    if N == 0:
        print('NULL')
