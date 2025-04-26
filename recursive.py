# I ask the user to enter a number
n = int(input("Enter the number: "))

# I define a function called factorial that takes n as the input
def factorial(n):
    if n == 0 or n == 1:# If n is 0 or 1, the recursion stops nd returns 1.
        # Because 0! = 1 ans 1! = 1.
        return 1
    else:
        # This is the recursive case
        return n * factorial(n-1)# This means that the function calls itself with a smaller number (n-1).

# Now i print the result.
print(factorial(n))