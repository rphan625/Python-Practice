""" Exercise 4
    Divisors
    Asks user for number, print list of all divisors
"""

user_num = int(input("Enter a number: "))


def divisors(num):
    num_list = range(1, num + 1)
    results = [x for x in num_list if num % x == 0]
    return results


print(divisors(user_num))
