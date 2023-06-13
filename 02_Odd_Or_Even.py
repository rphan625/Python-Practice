""" Exercise 2
    Odd Or Even
    Ask the user for number, print if even or odd
    Extras:
        If divisible by 4
        Ask user for 2 nums, one called num, 2nd to divide by, print
        if it divides evenly or not"""

num = int(input("Enter a number: "))
check = int(input("Enter second number: "))


def EvenOrOdd(number, check):
    if check == 0:
        print("You cannot divide by 0")
    if number % 4 == 0:
        print("Divisible by 4")
    elif number % check == 0:
        print(f"{num} divides evenly with {check}!")
    else:
        print(f"{num} doesn't divide evenly with {check}")


EvenOrOdd(num, check)
