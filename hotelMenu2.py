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
    total = 0
    while True:
        try:
            itm = int(input("Choose item number: "))
            qnt = int(input("Enter quantity: "))
            if itm == 1:
                price = 180
            elif itm == 2:
                price = 200
            elif itm == 3:
                price = 250
            elif itm == 4:
                price = 40
            elif itm == 5:
                price = 70
            elif itm == 6:
                price = 90
            elif itm == 7:
                price = 60
            elif itm == 8:
                price = 70
            elif itm == 9:
                price = 50
            elif itm == 10:
                price = 70
            else:
                print("Invalid item number. Please try again.")
                continue
            
            total += price * qnt
            
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

