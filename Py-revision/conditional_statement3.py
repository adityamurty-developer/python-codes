# nested if-elif
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    elif not has_id:
        print("ID required")
else:
    print("Underage")