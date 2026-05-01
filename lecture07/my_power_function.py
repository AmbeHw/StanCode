"""
File: my_power_function.py
Name: 黃文晴
-------------------------------
This program shows how to define
a custom function called my_power.

By implementing my_power(a, b),
we will practice writing our own
functions to perform a specific task.
"""


def main():
	print('This program prints a to the power of b.')
	a = int(input('a: '))
	b = int(input('b: '))
	print(my_power(a, b))


def my_power(a, b):
	a **= 2
	b **= 2
	return a + b


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
