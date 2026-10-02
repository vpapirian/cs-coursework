first = input("Enter a string: ")
second = input("Enter a string: ")
third = input("Enter a string: ")

if first <= second and first <= third:
    print(first)
    if second <= third:
        print(second)
        print(third)
    else:
        print(third)
        print(second)

elif second <= first and second <= third:
    print(second)
    if first <= third:
        print(first)
        print(third)
    else:
        print(third)
        print(first)

else:
    print(third)
    if first <= second:
        print(first)
        print(second)
    else:
        print(second)
        print(first)

