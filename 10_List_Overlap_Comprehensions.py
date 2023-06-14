""" Exercise 10
    List Overlap Comprehensions
    Return list that contains only common elements between two lists
    Extras:
        Randomly generate two lists to test this
"""

import random

a = [random.randint(1, 100) for _ in range(1, random.randint(10, 13))]
b = [random.randint(1, 100) for _ in range(1, random.randint(10, 13))]
overlap = [x for x in a if x in b]
result = []

print(f"{a}\n{b}")
# print(overlap)

for i in overlap:
    if i not in result:
        result.append(i)

print(result)
