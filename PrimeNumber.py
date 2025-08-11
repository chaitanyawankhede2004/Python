def prime(n):
	flg= True
	for i in range(2,n//2,2):
		if n%i==0:
			flg=False
			break
	return flg
	if flg:
		print("its a Prime number. ")
	else:
		print("its NOT a Prime number. ")

def lstOfPrimr(n):
	l=[]
	for i in (n):
		if prime(i):
			l.append(i)
	print(l)
n=eval(input("Enter number to find list till n:"))
lstOfPrimr(n)
