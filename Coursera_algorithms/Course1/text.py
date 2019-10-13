import random

x = [(random.randint(0, 5)) for _ in range(6)]
y = [(random.randint(0, 5)) for _ in range(6)]

a = list(zip(x, y))  # This produces list of tuples
print(a)