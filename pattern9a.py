n = int(input('enter a number'))

for i in range(n):
    if i == (n - 1):

        print(' ' * (i) + '*')
    else:
        print(' ' * (i) + '*' + ' ' * (2 * n - 2 * i - 3) + '*')
