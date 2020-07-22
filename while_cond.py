id=''
password=''
user=('neeraj')
pwd=('hi')
while id!= user and password!=pwd:
	id=input('input enter uname')
	password=input('input enter pwd')
	if id!=user:
		print('wrong user id')
	else:
		print('wrong password')