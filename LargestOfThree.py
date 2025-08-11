'''Write a program to find largest of 3 numberes
'''
a=eval(input("Enter 1st no:"))
b=eval(input("Enter 2nd no:"))
c=eval(input("Enter 3rd no:"))

if a>b:
	if a>c:
		print ("1st Numeber is largest")
	else:
		print ("3rd Numeber is largest")
else:
	if b>c:
		print ("2nd Numeber is largest")
	else:
		print ("3rd Numeber is largest")

if a<b:
	if a<c:
		print ("1st Numeber is smallest")
	else:
		print ("3rd Numeber is smallest")
else:
	if b<c:
		print ("2nd Numeber is smallest")
	else:
		print ("3rd Numeber is smallest")
		
		
if a>b and a>c:
	print (a,"is largest")
elif b>a and b>c:
	print (b,"is largest")
else:
	print (c,"is largest")
	
