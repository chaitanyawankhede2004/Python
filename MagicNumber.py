def MagicNum(n):
    chck, tm = n, 0
    while n != 0:
        tm += (n % 10) ** 3
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

