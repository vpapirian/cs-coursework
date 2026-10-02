import random

# Start at (0,0)
x = 0
y = 0

for i in range(100):
    direction = random.choice(["N", "E", "S", "W"])

    if direction == "N":
        y += 1
    elif direction == "S":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "W":
        x -= 1

print(f"The end location was ({x},{y}).")