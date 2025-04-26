# First I want to ask for a number from the user.
number = int(input("Enter a number: "))

# Now to check whether the number is even or odd.
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
# The % 2 is meant to find the remainder when a number is divided by 2
# If the remainder is 0, then it is even
# If the remainder is not 0 then it is odd
# % 2 == 0 is used to check if the remainder is 0.