dev = {"Chintu", "Sai", "Sushant", "Krish", "Arpit"}
anyl = {"Ayushi", "Chintu", "Sai", "Gauri Bhavri", "Mango"}

print("All the employees of the company:")
print(dev.union(anyl))

print("\nList of all Developers :")
print(dev)

print("\nList of all Analysts :")
print(anyl)

print("\nList of all Developers who are Analysts as well :")
print(dev.intersection(anyl))


print("\nList of all Analysts who are Developers as well :")
print(anyl.intersection(dev))


print("\nList of all Developers who arent Analysts :")
print(dev.difference(anyl))

print("\nList of all Analysts who arent Developers :")
print(anyl.difference(dev))

print("\nList of distinct employes :")
print(dev.symmetric_difference(anyl))
