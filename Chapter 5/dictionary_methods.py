marks = {
    "Harry": 100,
    "Aditya": 90,
    "Priya": 75,
    "Virat": 54,
}

print(marks.items())  # Return a list of (key, value) tuples

print(marks.keys())  # Return a list containing dictionary keys

marks.update({"Harry": 99, "Shreya": 82 })  # Updates the dictionary
print(marks)

print(marks.get("Priya"))  # Returns the value of a key and it is better than marks[key] method

marks.pop("Virat")  # Remove a specific key
print(marks)

marks.popitem()  # Remove the last key
print(marks)