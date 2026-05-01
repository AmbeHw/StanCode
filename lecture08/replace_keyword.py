"""
File: replace_keyword.py
Name:黃文晴
----------------------
This program demonstrates how to
replace an old word with a new word
in a given string by using the
replace() function.
"""


def main():
	old_s = input("Input a string:")
	old_word = input("Input the word you want to replace:")
	new_word = input("Input a word replacing the old word:")
	print(replace(old_s, old_word, new_word))



def replace(old_s, old_word, new_word):
	new_s = str()
	dif = ord(new_word) - ord(old_word)
	for char in old_s:
		if char == old_word:
			new_s += chr(ord(char) + dif)
		else:
			new_s += char
	return new_s


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
