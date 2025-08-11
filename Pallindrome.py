def pal():
	n=int(input("Enter No to check Palinddrome :"))
	temp=n
	rev=0
	while (n!=0):
		rev=rev*10+n%10
		n=n//10
	
	if rev==temp:
		print("It is a palindrome")
	else:
		print("It is NOT a palindrome")

pal()
pal()
pal()
	
