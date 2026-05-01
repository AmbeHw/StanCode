"""
File: guess_my_number.py
Name:黃文晴
-----------------------------
This program runs a console game
called "Guess My Number".

The program repeatedly asks the user
to guess a number until the correct
answer is given.
"""

# This number controls when to stop the game
SECRET = 32


def main():
    num = int(input("Guess My Number:"))
    while num != SECRET:
        num = int(input("Guess My Number:"))
    print("Bingo!")


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
