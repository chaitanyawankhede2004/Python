L=eval(input("Enter list L :"))
M=eval(input("Enter list M :"))
N=[]
if len(L)==len(M):
	for i in range(len(L)):
		N.append(L[i]+M[i])
else:
	print("Length of List is diffrent!!")
	
print(N)
