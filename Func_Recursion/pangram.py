import string
print()
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset

print(string.ascii_lowercase)

st = "The quick brown fox jumps over the lazy dog"

print("string --> ",st)
print("Is the string pangram ?? -->",ispangram(st))
