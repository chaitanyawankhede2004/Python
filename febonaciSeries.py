start = int(input("Enter starting point of series: "))
end = int(input("Enter end point of series: "))

n1, n2 = 0, 1
i = 0

fib= []

while i < end:
    if i >= start:
        fib.append(n1)
    n1, n2 = n2, n1 + n2
    i += 1
print("Fibonacci series from position", start, "to", end - 1, "is:")
for num in fib:
    print(num)

