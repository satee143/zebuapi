n=int(input('enter the range'))
t1=0
t2=1
sum=0
i=1
while( i<=n):
	
	sum=t1+t2
	t1=t2
	t2=sum
	print(sum,'\t',end='')
	i=i+1
