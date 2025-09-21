# multiplication_table.py
# multiplication_table.py

# Prompt user for a number
try:
    number = int(input("Enter a number to see its multiplication table: ").strip())
except ValueError:
    print("Invalid input! Please enter an integer.")
    exit()

# Generate and print multiplication table using a for loop
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
