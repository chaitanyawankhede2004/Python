marks = ()
for i in range(4):
    std = int(input(f"Marks of student {i+1}:"))
    marks = marks + (std,)

print(marks)


lst=[]
for i in range(5):
    std = int(input(f"Marks of student {i+1}: "))
    lst.append(std)
tup=tuple(lst)

print(tup)

