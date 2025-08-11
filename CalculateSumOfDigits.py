def cal():
	n=int(input("Enter no :"))
	sm=0
	while (n!=0):
		sm+=n%10
		n//=10	
	return sm

print(cal())
print(cal())
print(cal())
print(cal())

