# ----- Character Identifiers -----
# \d   -   Digit
# \w   -   Alphanumeric
# \s   -   white space
# \D   -   a non-digit
# \W   -   Non-alphanumeric
# \S   -   Non-white space

# ----- Quantifiers -----
# +   -   occurs one or more times
# {3} -   occurs exactly 3 time
# {2,4} - occurs 2 to 4 times
# {3,} -  occurs 3 or more
# *   -   occurs zero or more times
# ?   -   once or more


import re

text = 'My phone number is 408-555-1234'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)
print(phone.span())
print(phone.group())
print()

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
phone = re.search(r'\d{3}-\d{3}-\d{1}', text)
print(phone, end="\n\n")

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))
# print(results.group(4)) --- error as there is no 4th group
