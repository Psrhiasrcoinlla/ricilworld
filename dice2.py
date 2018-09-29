i=int(input("enter value of i: "))
j=int(input("enter value of j: "))
o=input("what do you want to do? +,-,x,/:")


def add():
	return a+b
def sub(a,b):
	return a-b
def mult(a,b):
	return a*b
def divide(a,b):
	return a/b

if(o=='+'):
	print("addition=",add(a,b))
elif(o=='-'):
	print("substraction=",sub(30,60))
elif(o=='x'):
	res=mult(i,j)
	print("multiplication=",res)
elif(o=='/'):
	print("division=",divide(a,b))


