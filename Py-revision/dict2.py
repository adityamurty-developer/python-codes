# Methods of dictionary:

student = {
    "name": "Rohan",
    "age": 20,
    "cgpa": 7.6
}

# 1. get() --> get is use to access values from dictionary

print(student.get("name"))  # Rohan
print(student.get("salary"))  # no key exist then output is: none

# we can also provide a default value
print(student.get("salary", 0))  # output will be default value if no key is exist

# get() vs []

# print(student["salary"]) --> this will give a keyError but get will give None or a default value

# 2. keys() --> returns all the keys of a dictionary
print(student.keys())

# 3. values() --> returns all the values of a dictionary
print(student.values())

# 4. items() --> return pairs of key-item
print(student.items())

# 5. update() --> add new key-value pairs or update the existing values
student.update({
    "age": 21,
    "skills": ["Py", "Cpp", "Dsa"]
})

print(student)

# 6. pop() --> removes a specific key and return its value

remove = student.pop("age")
print(remove)
print(student)  # we can also give a default value in case if key not existed

# 7. popitem() --> remove the last inserted key-pair 
remove = student.popitem()
print(remove)

# 8. clear() --> remove all the items 
student.clear()
print(student) # we will get a empty dictionary

# 9. copy() --> creates a separate copy of a dictionary

employee = {
    "name": "Rohan",
    "salary": 1200000,
    "company": "Google"
}

new_employee = employee.copy()
new_employee["salary"] = 1800000
new_employee["company"] = "Apple"

print(employee)
print(new_employee)

# 10. setdefault() --> if key not exist , key + default value will be added in dictionary

# it seems similar to get() with default value but with get() key will not be added

cars = {
    "car1": "TATA",
    "car2": "MAHINDRA",
    "car3": "TOYOTA"
}

print(cars.setdefault("car4", "MARUTI SUZUKI"))
print(cars)

# key exists --> existing value will be return, no change in dictionary
# key doesn't exist --> default value add + that value return