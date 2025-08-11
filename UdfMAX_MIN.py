'''wap to print the costliest item  and th cheapest item among 3 items'''

def max_3(a,b,c):
	if a>b and a>c:
		return "Item 1"
	elif b>a and b>c:
		return "Item 2"
	else:
		return "Item 3"

def min_3(a,b,c):
	if a<b and a<c:
		return "Item 1"
	elif b<a and b<c:
		return "Item 2"
	else:
		return "Item 3"

it1=int(input("Cost of Item 1 :"))
it2=int(input("Cost of Item 2 :"))
it3=int(input("Cost of Item 3 :"))

print("\nCostlist  :",max_3(it1,it2,it3))

print("\nCheapest :",min_3(it1,it2,it3))

