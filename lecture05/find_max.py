"""
File: find_max.py
Name:黃文晴
--------------------------
This program finds the maximum value
among all user inputs.

This file can be used as a reference
when working on Problem 4 in
Assignment 2.
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program finds the maximum among
    user inputs
    """
    num = int(input("Input a number:"))
    maxi = num
    while num != EXIT:
        if num > maxi:
            maxi = num
        num = int(input("Input a number:"))
    print(maxi)


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
