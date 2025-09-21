# pattern_drawing.py

# Prompt user for number of rows
try:
    rows = int(input("Enter the number of rows for the pattern: ").strip())
except ValueError:
    print("Invalid input! Please enter an integer.")
    exit()

# Initialize row counter
i = 1

# Outer loop for each row
while i <= rows:
    # Inner loop for printing stars in each row
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()  # Move to the next line after each row
    i += 1
