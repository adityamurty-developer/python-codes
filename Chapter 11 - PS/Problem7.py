class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


v1 = Vector(7, 8, 10)

print(v1 * 2)