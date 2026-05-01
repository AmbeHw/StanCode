"""
File: function.py
Name:黃文晴
-------------------------------
This program demonstrates essential
function concepts by using the
my_add and my_subtract functions.
"""


def main():
	num1 = int(input("Input first number:"))
	num2 = int(input("Input second number:"))
	add = my_add(num1, num2)
	sub = my_subtract(num1, num2)
	print(add, " ", sub)

def my_add(a, b):
	return a+b

def my_subtract(a, b):
	if a>=b:
		return a-b
	else:
		return b-a


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
