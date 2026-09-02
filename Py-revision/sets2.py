# Methods of sets

# 1. add() --> add one element in a set
nums = {10, 20, 30}
nums.add(40)
print(nums)

# 2. remove() --> remove a specified element
values1 = {10, 20, 30}
values1.remove(20)
print(values1)  # if element not present then keyError occurs

# 3. discard() --> it also remove a specified element but no error occurs eve if the specified element is not present 
values2 = {1, 2, 3}
values2.discard(4)
print(values2)

# 4. pop() --> removes and return an arbitrary element
marks = {40, 50, 60}
removed = marks.pop()  # it takes no argument
print(removed)
print(marks)

# 5. clear() --> remove all the element of a set

numbers = {10, 20, 30, 40}
numbers.clear()
print(numbers)