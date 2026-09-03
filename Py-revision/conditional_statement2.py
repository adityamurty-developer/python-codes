# nested if - else 

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("Id required")
else:
    print("Underage")