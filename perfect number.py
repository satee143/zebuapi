n = int(input('enter a number'))
s = 0
for i in range(1, n):
    if n % i == 0:
        s = s + i

if s == n:
    print('the number is perfect')
else:
    print('the number not perfect')
