L = eval(input("Enter numbers separated by space: "))

for i in L:
    print(i)

print(L[-1])

for i in L[::-1]:
    print(i)

src = int(input("Enter no to search :"))
if src in L:
    print("List contains", src)
else:
    print("Not available!!")

cnt = 0
for i in L:
    if i == src:
        cnt += 1
print(cnt)

L.remove(L[-1])
L.remove(L[0])
print(L)

L.sort()
print(L)
