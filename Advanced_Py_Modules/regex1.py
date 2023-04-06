text = "The agent's phone number is 408-555-1234. Call soon!"
print('phone' in text)


import re

pattern = 'phone'
match = re.search(pattern, text)
print(match)
print(re.search('aa', text))
print(match.span())
print(match.start())
print(match.end())

text = 'my phone once, my phone twice'
match = re.search('phone' ,text)
print(match)

matches = re.findall('phone', text)
print(matches)
print(len(matches))

for m in re.finditer("phone", text):
    print(m.group())
    print(m.span())
    

