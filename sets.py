# Set Creation
A = set([1, 2, 3, 4])
B = {3, 4, 5, 6}
print("Set A:", A)
print("Set B:", B)

# Set Union
union_set = A.union(B)
print("Union (A | B):", union_set)

# Set Intersection
intersection_set = A.intersection(B)
print("Intersection (A & B):", intersection_set)

# Set Difference
difference_set = A.difference(B)
print("Difference (A - B):", difference_set)

# Symmetric Difference
symmetric_diff_set = A.symmetric_difference(B)
print("Symmetric Difference (A ^ B):", symmetric_diff_set)

# Set Relations
print("A is subset of B:", A.issubset(B))
print("A is superset of B:", A.issuperset(B))
print("A and B are disjoint:", A.isdisjoint(B))

# Modifying Sets
print("\nOriginal Set A:", A)

A.add(7)
print("After add(7):", A)

A.discard(2)
print("After discard(2):", A)

A.remove(1)
print("After remove(1):", A)

# Pop an element
popped = A.pop()
print("After pop():", A, " (Popped:", popped, ")")

# Clear the set
A.clear()
print("After clear():", A)

# Set comprehension
squares = {x*x for x in range(6)}
print("Set comprehension (squares):", squares)

