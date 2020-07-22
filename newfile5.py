s = 'durga software'
l = []
for x in s:
    if x not in l:
        l.append(x)

print(l)
for m in range(len(l)):
    print(l[m], 'is appeared in ', s.count(l[m]), 'times')
