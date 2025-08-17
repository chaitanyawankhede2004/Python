import numpy as np

A = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix row by row:")
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

A = np.array(A)

x, y = map(int, input("Enter pixel coordinates (row col): ").split())
x -= 1
y -= 1

m, n = A.shape

adj4 = []
if x-1 >= 0: adj4.append((x-1, y))
if x+1 < m: adj4.append((x+1, y))
if y-1 >= 0: adj4.append((x, y-1))
if y+1 < n: adj4.append((x, y+1))

adj8 = adj4.copy()
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        if not (i == 0 and j == 0):
            p, q = x+i, y+j
            if 0 <= p < m and 0 <= q < n and (p,q) not in adj8:
                adj8.append((p,q))

adjM = adj4.copy()
for i in [-1, 1]:
    for j in [-1, 1]:
        p, q = x+i, y+j
        if 0 <= p < m and 0 <= q < n:
            if A[x, q] == 0 and A[p, y] == 0:
                adjM.append((p,q))

print("4-adjacency:", adj4)
print("8-adjacency:", adj8)
print("Mixed adjacency:", adjM)