def MagicNum(n):
    chck, tm = n, 0
    s=0
    rem,r=0,n
    while (r!=0):
    	rem+=1
    	r//= 10
    	
    while n != 0:
        tm += (n % 10) **rem
        n //= 10
    return tm == chck

def listOfMagicNum(x):
    l = []
    for i in range(x):
        if MagicNum(i):
            l.append(i)
    print("Magical numbers less than", x, "are:", l)

x = int(input("Enter a number: "))
listOfMagicNum(x)

