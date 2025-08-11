def Reverse():
	n=int(input("Enter no :"))
	res=0
	while (n!=0):
		res=res*10+n%10
		n=n//10	
	return res
print(Reverse())
print(Reverse())
print(Reverse())
