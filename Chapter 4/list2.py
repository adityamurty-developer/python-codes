friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends)

friends.append("Aditya")  # append means insertion at the end of the list
print(friends)

l1 = [1, 34, 62, 2 , 6, 11]

l1.sort()  # updates the list in sorted order
print(l1)

l1.reverse()  # reverse the list, here we will get the reverse of sorted list
print(l1)

l2 = [1, 56, 23, 7, 15]
l2.insert(3, 8)  # add 8 at index 3 --> (index, num_to_insert)
print(l2)

l3 = [12, 19, 47, 28, 84]
l3.pop(2)   # delete element at index 2 
print(l3)

l4 = [12, 19, 47, 28, 84]
l4.remove(28)
print(l4)