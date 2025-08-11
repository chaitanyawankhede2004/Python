nm=input("Enter a string:")

print("Total no of charecters are : ",len(nm))
print("string 10 times :\n\n",nm*10)

print("First Charecter : ",nm[0])
print("Last Charecter : ",nm[-1])

print("First 3 charecters : ",nm[0:4])
print("Last 3 charecters : ",nm[-3])
print("String Reverse :",nm[::-1] )
print("Removing fist and last charecter ;", nm[1:-1])

print(nm.replace('a','e'))
