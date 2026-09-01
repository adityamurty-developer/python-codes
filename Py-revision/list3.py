# List Methods

# 8. index() --> find index of  a value
nums1 = [10, 20, 30, 40]
print(nums1.index(20))

# --> returns the index of first occurrence 
# --> if value not existed in the list, valueError will occurs

# 9. count() --> finds the total occurrence of a value
nums2 = [10, 20, 30, 20, 40, 20]
print(nums2.count(20))

# --> if value not existed, then 0 will be returned

# 10. clear() --> it removes all the elements from a list
nums3 = [10, 20, 30, 40]
nums3.clear()
print(nums3)

# 11. del --> it is a python keyword, and it can delete either a entire list or multiple elemetns using list slicing or delete a specific element using index
list1 = [10, 20, 30, 40]
del list1[2]
print(list1)

list2 = [10, 20, 30, 40]
del list2[1: 4]
print(list2)

list3 = [10, 20, 30, 40]
del list3
# print(list3)  # it will give a name error 