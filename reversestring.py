n = input('enter the word for your choice')

s = ''
for x in n:

    if x != ' ':
        s = s + x
print(s[-1::-2])
