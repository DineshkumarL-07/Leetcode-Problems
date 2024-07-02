# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true

def toSquareNumber(num):
    sum = 0
    while num > 0:
        rem = num % 10
        sum += (rem**2)
        num //= 10
    return sum


def isHappy(num):
    visit = set()
    while num != 1 and num not in visit:
        visit.add(num)
        num = toSquareNumber(num)
    return True if num == 1 else False

num = int(input("Enter the Number: "))
print(isHappy(num))