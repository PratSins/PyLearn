dict1 = {"apple": 1, "banana": 2}
dict2 = {"orange": 3, "pear": 4}
print("dict1 - ",dict1)
print("dict2 - ",dict2)

dict1.update(dict2)
print("\ndict1.update(dict2)")
print("dict1 - ",dict1)
print("\n-----------------------------------\n")


dict1 = {"apple": 1, "banana": 2}
dict2 = {"orange": 3, "pear": 4}
print("dict1 - ",dict1)
print("dict2 - ",dict2)


merged_dict = {**dict1, **dict2}
print("\nmerged_dict = {**dict1, **dict2}")
print("merged_dict - ",merged_dict)
