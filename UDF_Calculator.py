def add(a,b):
	print(a," + ",b," = ",a+b)
	
def sub(a,b):
	print(a," - ",b," = ",a-b)

def mul(a,b):
	print(a," * ",b," = ",a*b)

def div(a,b):
	if b!=0:
		print(a,"/",b,"=",a/b)
	else :
		print("Cannot divide by Zero .")
def mod(a,b):
	print ("Modulus of ",a , "," , b ," =" ,a%b)

print("Calculator\n")

a=eval(input("Enter Num 1 :"))
b=eval(input("Enter Num 2 :"))

while True:

	print('''Enter Choices among follow :
	1. Addition
	2. Subtraction 
	3. Multiplication
	4. Division
	5. Modulus''')
	ch=int(input("Enter Choice : "))
	if ch==1:
		add(a,b)
	elif ch==2:
		sub(a,b)
	elif ch==3:
		mul(a,b)
	elif ch==4:
		div(a,b)
	elif ch==5:
		mod(a,b)
	else:
		print("Wrong Choice !!!!")
		
	cnt=input("Want to continnue Y-1/N-0")
	if cnt in "yY":
		continue
	else:
		break
	
	
	
	
