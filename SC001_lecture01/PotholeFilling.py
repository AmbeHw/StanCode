"""
File: PotholeFilling.py
Name: 黃文晴
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99beeper()
        go_out()
def go_in():
    move()
    turn_right()
    move()
def go_out():
    turn_around()
    move()
    turn_right()
    move()
def turn_right():
    for i in range(3):
        turn_left()
def turn_around():
    for i in range(2):
        turn_left()
def put_99beeper():
    for i in range(2):
        put_beeper()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
