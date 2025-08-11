A = {200, 300, 400, 500, 600, 700}
B = {200, 301, 405, 504, 700, 1000}
C = {200, 700, 600, 299, 185}

print("List of Prices of all items sold by A, B and C:")
print(A.union(B.union(C)))

print("\nList of prices of common items sold by A, B and C:")
print(A.intersection(B.intersection(C)))

print("\nList of distinct prices:")
print(A.symmetric_difference(B.symmetric_difference(C)))

print("\nList of prices of common items sold by A and B:")
print(A.intersection(B))

print("\nList of prices of common items sold by B and C:")
print(B.intersection(C))

