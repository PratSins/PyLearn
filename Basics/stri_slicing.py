a = "Harry's" 
b = "Harry's"
c = '''Harry"s and Harry's'''

print(a+"\n"+b+"\n"+c)

print("Lenght of string a = ",len(a))
d= "Prat"

print(d[-4])

# d[1] = 'a' --> Doesn't work

print(d[0:3])
print()

name = 'prat' # length = 4

print(name[:4]) # is same as name[0:4]
print(name[0:]) # is same as name[Q:4]

k = name[-4:-1]
print("name[-4:-1] =",k)

np = 'HarryIsGood'
d = np[0::2]
print("np[0::2] =",d)
kd = np[0:4]
d = np[0:4:3]   # 1st and 2nd number represent position just like normal slicing... 3rd one is for no. of characters to skip
               # if 3rd no. is 3 then 2 characters are skipped
print("np[0:4]  =  ",kd)
print("np[0:4:3] =  ",d)