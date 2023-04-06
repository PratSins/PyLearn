from collections import Counter
# Counter is a Dictionary sub-class
print("\n---Counter with list")
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]
print( Counter(mylist) )

mylist2 = ['a','a',10,10,10]
print( Counter(mylist2) )

print("\n---Counter with a word")
print( Counter("aaabbbbPratcccttrrpp") )

print("\n---Counter with a sentence using split()")
sentence = "How many times does each word show up in this sentence with a word"
print(Counter(sentence.lower().split()))
