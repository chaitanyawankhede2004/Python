'''Write a program to check temprature entered by student 
using else-if lader for 5 times
'''
for i in range(5):
	temp = float(input("Enter Temperature in Celsius: "))
	if temp < -273.15:
	    print("Invalid Temperature (below absolute zero!)")
	elif temp == -273.15:
	    print("Absolute Zero Temperature")
	elif temp < 0:
	    print("Below Freezing Temperature")
	elif temp == 0:
	    print("At Freezing Temperature")
	elif temp > 0 and temp < 24:
	    print("Cold Temperature")
	elif temp >= 24 and temp <= 27:
	    print("At Room Temperature")
	elif temp > 27 and temp < 100:
	    print("Below Boiling Temperature")
	elif temp == 100:	
	    print("At Boiling Temperature")
	else:
	    print("Above Boiling Temperature")

