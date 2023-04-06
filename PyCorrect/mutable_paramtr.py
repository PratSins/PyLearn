
def Mutable_parameter(lst= []):
    lst.append (1)
    lst.append (2)
    return lst

# def Mutable_parameter(lst= None):
#     if lst == None:
#         lst =[]
#     lst.append (1)
#     lst.append (2)
#     return lst

print(Mutable_parameter())
print(Mutable_parameter())
print(Mutable_parameter())

