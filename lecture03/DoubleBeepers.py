"""
File: DoubleBeepers.py
Name:黃文晴
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    while front_is_clear():
        move()
        if on_beeper():
            double_it()

def double_it():
    num = 0
    while on_beeper():
        pick_beeper()
        num = num + 1
    num = num +num
    for i in range(num):
        put_beeper()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
