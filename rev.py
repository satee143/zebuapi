s=input('Enter word')
l=-1
a=0
r=[]
t=-len(s)
for i in s:
	while l>=t  :
		r.append(i)
		l=l-1
		a=a+1
print(r)
