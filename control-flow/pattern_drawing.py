# pattern_drawing.py

# Prompt user for pattern size (exact prompt text)
size = int(input("Enter the size of the pattern:"))

# Initialize row counter
i = 1

# Outer loop for each row
while i <= size:
    # Inner loop for printing stars in each row
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()  # Move to next line
    i += 1
