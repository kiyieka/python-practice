# Ask the user to type any string
text = input("Enter text: ")

# I create an empty  string where I'll  build the reversed version
reversed_text = ""

# I used a for loop to go through each character one by one from left to right
for char in text:
    reversed_text = char + reversed_text# Instead of adding the character to the end of reversed_text,
    # i added each new character to the beginning.

# Now i print the fully reversed string.
print("The reversed string is:", reversed_text)