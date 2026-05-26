class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)

    def __mul__(self, v2):
        return Vector(self.x * v2.x, self.y * v2.y)

    def __str__(self):
        return f"({self.x}i, {self.y}j)"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
print(v1 * v2)