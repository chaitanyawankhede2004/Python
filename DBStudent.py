DataBase = []
n = int(input("Enter number of student data: "))
for i in range(n):
    print("Details of student", i + 1)
    usn = input("Enter USN number: ")
    nm = input("Enter student Name: ")
    cont = input("Enter Contact Number: ")
    stream = input("Enter stream: ")
    percent = eval(input("Enter Percentage: "))
    DataBase.append((usn, nm, cont, stream, percent))
print("\n############# Print Data-Base #############\n")
for record in DataBase:
    print(record)
for i in range(len(DataBase)):
    for j in range(0, len(DataBase) - i - 1):
        if DataBase[j][4] < DataBase[j + 1][4]:
            DataBase[j], DataBase[j + 1] = DataBase[j + 1], DataBase[j] #swapping krra hai
print("\nSorted Data:")
for record in DataBase:
    print(record)

