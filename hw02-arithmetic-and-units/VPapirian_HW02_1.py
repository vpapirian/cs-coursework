## Setting the variables for user to input numbers

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a second number: "))

total: int =  number_1 + number_2           ## dding the ints
difference: int = number_2 - number_1       ## subtracting the ints
product: int  = number_1 * number_2         ## multiplying the ints
avg: float = total / 2                      ## finding the average
max_num = max(number_1, number_2)           ## finding the max
min_num = min(number_1, number_2)           ## finding the min


## This is just the code to print the previous arithmetic

print("Total = ", total)
print("Difference = ", difference)
print("Product = ", product)
print(f"Average = ", f"{avg:.2f}")
print("Max Number = ", max_num)
print("Min Number = ", min_num)






