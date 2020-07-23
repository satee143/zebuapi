from num2words import num2words


def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)


num = 5
f = (fact(num))
print(num2words(f, to='ordinal', lang='en'))
