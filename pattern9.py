n = int(input('enter a number'))
for i in range(n):
    print(' ' * (n - i - 1) + '*', end='')
    if i > 0:
        print(' ' * (2 * i - 1) + '*')
    print()
