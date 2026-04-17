import re

s = input("Enter a string: ")

pattern = r'^([a-z]).*\1$|^[a-z]$'

"""
^[a-z]$ -> Matches a single lowercase letter
^([a-z]).* -> Captures first lowercase letter
.* -> Any characters in between
\1 -> Same character at the end
"""

if re.match(pattern, s):
    print("String starts and ends with the same character.")
else:
    print("String does not start and end with the same character.")
