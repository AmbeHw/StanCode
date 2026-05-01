"""
File: my_upper.py
Name:黃文晴
----------------------
This program demonstrates how the
Python built-in method s.upper()
can be implemented.

By recreating its behavior step by
step, we will better understand how
string methods work internally.
"""


def main():
	s = '123JeRrY123'
	print(upper(s))


def upper(s):
	st = str()
	for i in range(len(s)):
		if 97 <= ord(s[i]) <= 122:
			st += chr(ord(s[i]) - 32)
		else:
			st += s[i]
	return st


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
