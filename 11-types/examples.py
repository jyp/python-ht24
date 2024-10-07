# while True:
#     print("waiting...")

import math

x : int
x = 7

y : float
y = x # math.pi

def greeting(name : str) -> str:
    return 'Hello ' + name

def print_greeting(name: str) -> None:
    print('Hello ' + name)

# print_greeting("Bob")

def squaring(z: float) -> float:
    return z*z

def identity(x: object) -> object:
    return x
    
# print(squaring(y))

l1 : list[int]
l1 = [1,2,3]

x = l1.pop(1)
print(l1, x)

print(reversed(["hello", "world"]))

# l2 : list[float]
# l2 = l1

t1 : tuple
t1 = (1,2,3)

# print(len(l1))
# print(len(t1))
