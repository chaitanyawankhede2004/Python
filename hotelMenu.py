def PrintMenu():
    print("************ Menu **********")
    print("Main Course:")
    print("1- Special Thali - 180")
    print("2- Premium Thali - 200")
    print("3- Nonveg Thali - 250")
    print("\nStarters:")
    print("4- Masala Papad - 40")
    print("5- Cheese Corn - 70")
    print("6- Crispy Veg - 90")
    print("\nDessert:")
    print("7- Rasgulla - 60")
    print("8- Ice-cream - 70")
    print("9- Gulab Jamun - 50")
    print("10- Rabdi - 70")
    print("\nEnter your order:")

def BillAmt():
	prices = {1: 180, 2: 200, 3: 250, 4: 40, 5: 70, 6: 90, 7: 60, 8: 70, 9: 50, 10: 70}
	total = 0
	while True:
		try:
			itm = int(input("Choose item number: "))
			qnt = int(input("Enter quantity: "))
			if itm in prices:
				total += prices[itm] * qnt
			else:
				print("Invalid item number. Please try again.")
				continue
		except ValueError:
			print("Invalid input. Please enter numeric values.")
			continue

		ch = input("Add more items? (Y/n): ")
		if ch.upper() != "Y":
			print("Thanks for the order!")
			break
	return total

def Bill():
    print("************* Bill Receipt **************")
    print("Total amount: ", BillAmt())
    print("Thanks for visiting!")

PrintMenu()
Bill()

