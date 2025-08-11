items = []
n=int(input("Enter no. of Items to enter :"))
for i in range(n):
    shop = {}
    shop["Name"] = input("Enter Name of item: ")
    shop["ItemNo"] = int(input("Enter Item Number: "))
    shop["Price"] = float(input("Enter Price: "))
    shop["Stock"] = input("Enter Availability: ")
    items.append(shop)  
    print(shop)

print("\nAll items:")
print(items)

for i in items:
    print(i)

