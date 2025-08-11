
end = int(input("Enter end point of series: "))

n1, n2 = 0, 1
i = 0
fib= []
tem=[]
while i < end:
	fib.append(n1)
	n1, n2 = n2, n1+n2
	i += 1
for j in range(1,len(fib),2):
	tem.append(fib[j])
	print(j)
print(fib)
print(tem)
