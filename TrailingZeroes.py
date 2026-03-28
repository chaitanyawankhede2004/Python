# Problem: Find the number of trailing zeros in (100! + 125!)

def trailing_zeros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

zr_100 = trailing_zeros(100)
zr_125 = trailing_zeros(125)

result = min(zr_100, zr_125)

print(result)