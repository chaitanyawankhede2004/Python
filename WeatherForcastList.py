temp = [30, 35, 34, 34, 35, 36, 36, 37, 37, 30, 45, 45, 23, 40]

def averageOfTemp():
    av = 0.0
    for i in temp:
        av += i
    average = av / len(temp)
    return average

def overAverage():
    avg = averageOfTemp()
    cnt = 0
    for i in temp:
        if i > avg:
            cnt += 1
    return cnt

def highestTemp():
    mx = temp[0]
    for i in temp:
        if mx < i:
            mx = i
    return mx

def lowestTemp():
    mn = temp[0]
    for i in temp:
        if mn > i:
            mn = i
    return mn

def diffOfTemp():
    return highestTemp() - lowestTemp()

while True:
    print("\n#########  Company Temp  ###########")
    print("Perform Task:")
    print("1 - Find Average")
    print("2 - Number of days with above average temp")
    print("3 - Highest Temp")
    print("4 - Lowest Temp")
    print("5 - Difference between Highest and Lowest")
    print("6 - Exit")

    ch = int(input("Enter number to perform: "))

    if ch == 1:
        print("Average Temperature =", averageOfTemp())
    elif ch == 2:
        print("Number of days with temperature above average =", overAverage())
    elif ch == 3:
        print("Highest Temperature =", highestTemp())
    elif ch == 4:
        print("Lowest Temperature =", lowestTemp())
    elif ch == 5:
        print("Difference between highest and lowest temperature =", diffOfTemp())
    elif ch == 6:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 to 6.")

