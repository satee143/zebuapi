age = int(input('enter your age'))
if age < 0 or age == type(str):
    while True:
        print('flash, please enter correct')
        age = int(input('enter age again'))
        if 0 < age:
            break
elif 0 < age >= 3:
    print('ticket is 100')
else 4 < age >= 10:
    print('ticket is 200')
