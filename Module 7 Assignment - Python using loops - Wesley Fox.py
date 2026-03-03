# Program: Odd or Even Number Detector
# Author: Your Name
# Date: Current Date
# Description: This program creates a list of 15 numbers and uses a for loop
#              to determine if each number is odd or even, then prints the result.

# Create a list of 15 numbers
numbers = [3, 8, 12, 15, 22, 27, 31, 40, 45, 52, 57, 63, 70, 74, 89]

# Print a header
print("Odd/Even Number Checker")
print("-" * 40)

# Loop through each number in the list
for number in numbers:
    # Check if the number is even (divisible by 2 with no remainder)
    if number % 2 == 0:
        # Number is even - convert number to string for concatenation
        print(str(number) + " is even")
    else:
        # Number is odd - convert number to string for concatenation
        print(str(number) + " is odd")

# Print a footer
print("-" * 40)
print("Program complete!")
