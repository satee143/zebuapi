import random,string

fname=input('Enter your first bame')
lname=input('Enter your last name')
email=input('enter your email')

def randm(sl=5):
	

	letter=string.ascii_letters

	return  ''.join(random.sample(letter,sl))
#print(randm())
up=(str((fname[0:2]+lname[0:2]+str(randm()))))
print('we suggedted this pwd for u',up)