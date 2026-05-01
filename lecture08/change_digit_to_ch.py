"""
File: change_digit_to_ch.py
Name:黃文晴
----------------------
The goal of this program is to perform
a simple string transformation.

It takes a string containing both
digits and letters, and converts each
digit into its corresponding uppercase
letter (1 → A, 2 → B, 3 → C, and so on).

For example, the string "123abcab3b2"
will be transformed by replacing the
digits with letters following this
pattern.
"""


def main():
    mystery = '123abcab3b2'
    ans2 = digit_to_ch(mystery)
    print(ans2)  #ABCabcabCbB
    
    s = '11a22b33c'
    print(digit_to_ch(s))  # 'AAaBBbCCc'

def digit_to_ch(s):
    st = str()
    for i in range(len(s)):
        if 49 <= ord(s[i]) <= 57:
            st += chr(ord(s[i]) + 16)
        else:
            st += s[i]
    return st




if __name__ == '__main__':
    main()