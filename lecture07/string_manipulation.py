"""
File: string_manipulation.py
Name: 黃文晴
----------------------------
The goal of this program is to change
"stancode" to "stanCode".

Through this example, students will
practice basic string manipulation
using the following steps:
(1) Start with an empty string
(2) Loop over the original string
(3) Build a new string by concatenation
"""


def main():
	s = 'stancode'
	st = str()
	for i in range(len(s)):
		if s[i] == 's' or s[i] == 'c':
			st += chr(ord(s[i]) - 32)
		else:
			st += s[i]
	print(st)



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
