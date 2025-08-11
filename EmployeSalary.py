def readData():
	global nm,dept,desg,empId
	nm=input("Enter Name \t\t:")
	dept=input("Enter Department \t:")
	desg=input("Enter Designation \t:")
	empId=input("Enter Employee Id \t:")
	salary()
	
def salary():
	global bs,gs
	hra,pa,ba=0.4,0.3,0.9
	inc,lic,pf,tds=5000,2000,2400,800
	bs=eval(input("Enter Basic Salary :\t"))
	gs=bs+ bs*(hra	+ pa + ba  )- inc - lic -pf -tds

def disp():
	print("\n********************************************************\n")
	print("Name of Employe \t: ",nm)
	print("Department of Employe \t: ",dept)
	print("Designation of Employe \t: ",desg)
	print("Employe ID of Employe : ",empId)
	print("Basic Salry of Employe : ",bs)
	print("Gross salary of Employe : ",gs)
	
readData()
disp()

