# pattern_drawing.py

# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to handle rows
while row < size:
    # Use for loop to print columns of asterisks
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
