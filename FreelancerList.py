clients = []
working_hours = []
rates = []

n = int(input("Enter number of clients: "))

for i in range(n):
    name = input(f"Enter name of Client {i+1}: ")
    clients.append(name)

    hours = int(input(f"Enter hours worked for {name}: "))
    working_hours.append(hours)

    rate = int(input(f"Enter hourly rate for {name}: "))
    rates.append(rate)

income = 0
for i in range(n):
    income += working_hours[i] * rates[i]

print("Total Income = $", income)

