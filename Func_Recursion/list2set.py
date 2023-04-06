def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number )
    return seen_numbers


# The following is more efficient
# def unique_list(lst):
#     return list(set(lst))

mylst = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(mylst)



