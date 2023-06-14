""" Exercise 6
    Ask user for string, palindrome?
"""

user_string = str(input("Enter a possible palindrome: "))


def isPalindrome(string):
    if user_string == user_string[::-1]:
        return True
    else:
        return False


if isPalindrome(user_string):
    print(f"{user_string} is a palindrome!")
else:
    print(f"{user_string} is not a palindrome.")
