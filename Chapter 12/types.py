# types annotations

n: int = 5

name: str = "Harry"

def sum(a: int, b: int) -> int:
    return a+b

print(n.bit_count())

print(name.capitalize())
print(name.lower())

print(sum(3, 5))