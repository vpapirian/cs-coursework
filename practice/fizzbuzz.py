question = int(input("Put a number 1 - 100"))

for i in range(1, question + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)


for i in range(5, 26, 5):
    print(i, end=" ")



i = 20

while i >= 10:
    print(i, end=" ")
    i -= 2


for i in range(1, 15):
    if i % 4 == 0:
        print(i, end=" ")