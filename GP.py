# Problem: Find the next term in the sequence 3, 9, 27, 81

sel = [3, 9, 27, 81]

# Common ratio
r = sel[1] // sel[0]

nextTrm = sel[-1] * r

print(nextTrm)