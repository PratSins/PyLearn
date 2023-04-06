import re

match = re.search(r'cat|dog','The dog is here')  # Search is for <cat> OR <dog>
print(match)

m1 = re.findall(r'at','The cat in the,hat sat there.')
print(m1)
m2 = re.findall(r'.at','The cat in the,hat sat there.')
print(m2)

m3 = re.findall(r"...at","The cat hat splat sat hdhat")
print(m3)

m4 = re.findall(r"...at","The cat hat splat r sat hdhat")
print(m4)

m5 = re.findall(r"^\d","2 A ff 1 1dq 2 jfd 2www 1")
print(m5)
m6 = re.findall(r"\d$","2 A ff 1 1dq 2 jfd 2www 1")
print(m6)

 
print()
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pat = r'[^\d]'   # [] - excludes
m7 = re.findall(pat, phrase)   # 3 and 34 will be shown as blank spaces
print(m7)
pat2 = r'[^\d]+' 
m8 = re.findall(pat2, phrase)
print(m8)
print()

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
m9 = re.findall(r'[^!.?]+',test_phrase)
print(m9)
# m10 = re.findall(r'[!.?]+',test_phrase)
# print(m10)
m11 = re.findall(r'[^!.? ]+',test_phrase)
print(m11)
print()

m12 = ' '.join(m9)
print(m12)
print()

p1 = 'Only find the hypen-words in this sentence. But you do not know how gjyg-fsfgs'
ptt = r'[\w]+'
m13 = re.findall(ptt, p1)
print(m13)
print()

ptt1 = r'[\w]+-[\w]+'
ptt2 = r'[\w]-[\w]'
ptt3 = r'\w+-\w+'
m14 = re.findall(ptt1, p1)
m15 = re.findall(ptt2, p1)
m16 = re.findall(ptt3, p1)
print(m14)
print(m15)
print(m16)
