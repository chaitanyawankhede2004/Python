item = (101, 255, 55, 50, 101, 40, 48, 68, 99, 199, 299)
def Costliest():
    mx = item[0]
    for i in item:
        if i > mx:
            mx = i
    print("Maximum:", mx)
def Cheapest():
    mn = item[0]
    for i in item:
        if i < mn:
            mn = i
    print("Cheapest item of the tuple:", mn)
def totalItem():
    l = 0
    for i in item:
        l += 1
    print("Total items of Bill:", l)
def cntOf101():
    cnt = 0
    for i in item:
        if i == 101:
            cnt += 1
    print("Count of 101 in tuple:", cnt)
totalItem()
cntOf101()
Cheapest()
Costliest()
