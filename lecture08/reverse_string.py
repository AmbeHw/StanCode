"""
File: reverse_string.py
Name: 黃文晴
----------------------------
The goal of this program is to
reverse the string "stressed".

By doing so, we will observe
a fun and interesting result
while practicing string manipulation.
"""


def main():
	"""
	This program reverses 'stressed'
	"""
	old_str = 'stressed'
	new_str = reverse(old_str)
	print('The reversed string of ' + old_str + ' is: ' + new_str)

def reverse(old_str):
	new_str = str()
	for i in range(len(old_str)):
		new_str = old_str[i] + new_str
	return new_str
	

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
