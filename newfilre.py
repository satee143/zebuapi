n = int(input('enter a num'))
for i in range(n):
    for j in range(n, i, -1):
        print('*', end=' ')
    print()
