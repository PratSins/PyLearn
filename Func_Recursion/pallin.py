def palindrome(s):
        # REMOVE SPACES STRING
    s = s.replace(' ','')
        # Check is string is == reversed version of the string
    return s == s[::-1]


st = input("Enter a string:")

if palindrome(st):
    print("Its a pallindrome")
else:
    print("Its NOT a pallindrome")