l1=[]
for i in range(1,11):
	l1.append(i)

print(l1)

l2=[]
for i in range(11,21):
	l2.append(i)
print(l2)

l1.extend(l2)
print(l1)

