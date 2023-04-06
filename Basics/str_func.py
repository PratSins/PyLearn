story = "once upon a time there was FE youtuber named Harry who uploaded python course with notes"
print(story)
print()

# String Functions
print(len(story))
print(story.endswith( "notes" ))
print(story.count("a")) # return no of 'a' in the whole string
print(story.count("qq"))
print()

print(story.capitalize( ) , end="\n\n") # capitalizes 1st letter and makes other alphabets lowercase

print(story.find("upl")) # position of first occurence 
print(story.replace("Harry", "CodeWithHarry"), end="\n\n")

k = "Hello! k World!"
d = k.split('k')
print(d, end="\n\n")

print('a', end="")
print('ss', end="")
