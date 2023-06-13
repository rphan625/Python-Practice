""" Exercise 3
    List Less Than Ten
    Print all elements less than 10
    Extras:
        Ask user for number, return list of elems less than number
"""

import random

num_list = [random.randint(1, 20) for x in range(10)]
result = []
print(num_list)

# limit = 10

limit = int(input("Enter a number between 1-20: "))

result = [x for x in num_list if x < limit]

# for i in num_list:
#     if i < limit:
#         result.append(i)

print(f"This list has the numbers less than {limit}\n{result}")
