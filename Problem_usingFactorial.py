#1
def fact(n):
	if n!=0:
		return n * fact(n-1)
	else:
		return 1
def series1(n):
	sm=0
	for i in range(n,0,-1):
		sm=sm+fact(i)
	print("Sum of factorials upto series(n): ",sm)

def series2(m):
	sm=0
	for i in range(m,0,-1):
		sm=sm+fact(i-1)
	print("Sum of factorials upto sec series(n): ",sm)
	
n=int(input("N="))
series1(n)
m=int(input("N="))
series2(m)

	
