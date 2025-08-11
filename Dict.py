capitals = {
"Maharashtra":"Mumbai", 
"Gujarat":"Gandhinagar", 
"Telangana":"Hyderabad", 
"Karnataka":"Bengaluru"
}
numbers = {
10:"Ten", 
20:"Twenty", 
30:"Thirty",
40:"Forty"}
marks = {"Savita":67, 
"Imtiaz":88, 
"Laxman":91,
 "David":49}
print("Capitals of States : ",capitals)
print("States : ",capitals.keys())
print("Capitals: ",capitals.values())
print()
print("Numbers : ",numbers)
print("Digit : ",numbers.keys())
print("Spell : ",numbers.values())
print()
print("Marks :",marks)
print("Marks :",marks.keys())
print("Marks :",marks.values())
for key in capitals.keys():
	print(key)
print()
for key in numbers.keys():
	print(key)
print()
for key in marks.keys():
	print(key)
print()
for val in capitals.values():
	print(val)
print()
for val in numbers.values():
	print(val)
print()
for val in marks.values():
	print(val)
print()
print("Serching")
if "Maharashtra" in capitals:
	print("Maharashtra is available.")
	
if "Laxman" in marks:
	print("Laxman is available.")
	
if 10 in numbers:
	print("10 is available.")
