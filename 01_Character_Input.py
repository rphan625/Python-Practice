""" Exercise 1 Character Input
    Character Input
    Ask a user for name and age, tell them when they will turn 100 years old
"""

from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

till100 = 100 - age
currentyear = datetime.now().year

msg = "You will be 100 at year " + str(currentyear + till100)
print(msg)

repeat = int(input("Enter a number: "))

for _ in range(repeat):
    print(msg)
