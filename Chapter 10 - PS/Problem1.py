class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 1200000, 1234)
print(p.name, p.salary, p.pin)

r = Programmer("Rohan", 800000, 1235)
print(r.name, r.salary, r.pin)

s = Programmer("Priya", 650000, 1233)
print(s.name, s.salary, s.pin)