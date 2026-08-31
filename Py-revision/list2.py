# List Method's

# 1. append() --> insert an element at the end of a list
nums1 = [10, 20, 30]
nums1.append(40)
print(nums1)

# 2. extend() --> multiple elements can be added at a time
nums2 = [10, 20, 30]
nums2.extend([40, 50])
print(nums2)

# main difference --> appends can add only one element even it's a list, but extend can add multiple and add elements of a list individually

# 3. insert() --> adds element at a specific position
nums3 = [10, 30, 40]
nums3.insert(1, 20)
print(nums3)

# 4. remove() --> removes the first occurrence of the given value 
nums4 = [10, 20, 30, 20]
nums4.remove(20) # removes 1st occurrence of 20 i.e. from 1st index
print(nums4)

# 5. pop() --> removes element on the basis of index also it can return the removed element. If index is not assigned, the last element will get removed and return.
nums5 = [1, 2, 3, 4]
x = nums5.pop(2)
print(f"{nums5} and the removed element is: {x}")

# 6. sort() --> modify the original list
list1 = [40, 10, 30, 20]
list1.sort()
print(list1)  # sorted in ascending order 

list2 = [20, 10, 40, 30]
list2.sort(reverse=True)
print(list2) # sorted in descending order

# 7. sorted() --> returns new sorted list
list3 = [40, 10, 30, 20, 50]
new_list = sorted(list3, reverse=True)
print(f"original list is: {list3} and sorted list is: {new_list}")