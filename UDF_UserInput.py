def read():
	global name,usn,gmail
	name=input("Enter Name of student :")
	usn=input("Enter USN of student :")
	gmail=input("Enter G-Mail of student :")
	print("Data Readed Succesfully !!")

def display():
	print("Name\t:",name)
	print("USN\t:",usn)
	print("G-Mail\t:",gmail)
	

read()
display()
	
