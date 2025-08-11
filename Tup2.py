def Max():
	mx=tup[0]
	for i in tup:
		if i>mx:
			mx=i
	
	print("Maximum marks obtain : ", mx)

def Min():
	mn=tup[0]
	for i in tup:
		if i<mn:
			mn=i
		
	print("Minimum marks obtain : ", mn)

def avg():
	sm=0
	for i in tup:
		sm+=i
	return sm/n
	
def passPer():
	cntP=0
	for i in tup:
		if i>= (50):
			cntP+=1
	return (cntP/n)*100

lst=[]
n=int(input("Enter num of student :"))
for i in range(n):
	mrs=int(input(f"Enter marks of student{i+1} :"))
	lst.append(mrs)

tup=tuple(lst)

Max()
Min()
print("Average Marks :",avg())
print("Passing Percentage :",passPer())

