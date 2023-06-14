""" Exercise 5
    List Overlap
    Return list that contains elements that are common between lists
    without duplicates
"""

import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = [random.randint(1, 100) for _ in range(random.randint(10, 13))]
b = [random.randint(1, 100) for _ in range(random.randint(10, 13))]

result = []

for i in a:
    if i not in result:
        if i in b:
            result.append(i)

print(f"{a}\n{b}")

print(result)
