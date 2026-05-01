"""
File: receipt.py
Name:黃文晴
-------------------------
This program calculates the total cost
of a meal and prints the result to the
console.

Through this program, we will practice
using variables, taking user input, and
combining values into a single output
message.
"""


def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    total = num1 + num2
    print("The total is" + str(total) + ".")


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
