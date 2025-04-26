# First i ask the user for a number to find the factorial for
num = int(input("Enter a number: "))

factorial = 1 # Intialize the factorial result
i = 1

while i <= num: # Now compute the factorial using the while loop
    factorial *= i # I used the while loop, multiplying the factorial by i,
    # and then increasing i by 1 each time.
    i += 1# When i becomes greater than num the loop ends.

# Display the final factorial result
print("The factorial of", num, "is", factorial)