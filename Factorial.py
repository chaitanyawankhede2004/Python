def fact(n):
	if n!=0:
		return n * fact(n-1)
	else:
		return 1

n=int(input("Enter No. to find factorial :"))
print(fact(n))

def factorial(n):
	fac=1
	while (n!=0):
		fac=fac*n
		n-=1
		
	print("Factorial =",fac)
print("*****Recursive")
m=int(input("Enter No. to find factorial :"))
factorial(m)
