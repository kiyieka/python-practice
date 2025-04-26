# Ask for user input
num = int(input('Enter a number: '))

# I initiate the sum with 0 since every digit will be added onto this variable.
sum_of_digits = 0


while num > 0:# It keeps processing as long as the number is greater than 0.
    digit = num % 10 # This extracts the last digit of the remainder.
    sum_of_digits += digit# This adds the extracted digit to the running total.
    num //= 10# // IS THE FLOOR DIVISION OPERATOR.
    # It divides and drops any decimal part

# After the loop is done i print the total.
print(sum_of_digits)