# First, an example of a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I now initiate the total
# Since we have not added anything the total is then 0
total = 0

# I choose to loop through the list and add each element
# Here, it takes the first item and adds it to the total,
# and continues the loop adding the current total with
# the next number in the list until the list ends.
for number in numbers:
    total += number

# Now I print the total
print("The sum of the list is:",total)
