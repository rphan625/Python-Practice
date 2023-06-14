""" Exercise 7 
    List Comprehensions
    Take a list, return only even elements in one line
"""

a = [1, 4, 9, 16, 25, 36, 49, 81, 100]

result = [x for x in a if x % 2 == 0]

print(result)
