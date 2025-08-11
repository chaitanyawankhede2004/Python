print('''
****************************************
***********Programe Code**************
****************************************\n''')
InWall=int(input("\nEnter No of Interior Walls : "))
OutWall=int(input("Enter No of Exterior Walls : "))
OutArea=0
InArea=0
if (InWall !=0):
	InArea=int(input("Area of Interior wall (per Sq. Feet)\t:"))
if (OutWall !=0 ):
	OutArea=int(input("Area of Outer walls (per Sq. Feet )\t:"))
	
result= 18*InWall*InArea + 12*OutArea*OutWall

print("""
For Customer

Total Cost Requires is \t\t""",result) 
