#prompt the user for a positive integer n
#prints the following 3 items using a while loop:
#(1) all squares greater than zero and less than n

n = int(input("Enter a positive number: "))

num = 1
squared = num**2
while squared < n:
    print(squared, end = " ")
    num = num + 1
    squared = num**2
print()
#(2) all positive numbers that are divisible by 10 and less than n

n = int(input("Enter a positive number: "))

num = 10
while num < n:
    print(num, end=" ")
    num += 10

print()
#(3)  All powers of two greater than zero and less than n

n = int(input("Enter a positive number: "))

num = 1
power = 2**num
while power < n:
    print(power, end = " ")
    num = num + 1
    power = 2**num

print()

#prints the following 3 items using a for loop:
#(1) all squares greater than zero and less than n (HINT: use a nested if statement in the loop)

n = int(input("Enter a positive number: "))

num = 1
for num in range(1, int(n**0.5) + 1):
    squared = num ** 2
    if squared < n:
        print(squared, end = " ")
print()
#(2) all positive numbers that are divisible by 10 and less than n

n = int(input("Enter a positive number: "))

for num in range(10, n, 10):
    print(num, end = " ")

print()
#(3)  All positive multiples of two greater than zero and less than n

n = int(input("Enter a positive number: "))

for num in range(2, n, 2):
    print(num, end = " ")

print()
#For example: if the user enters 30 (n= 30)

#the program output should be:

#output from while loops:

#1 4 9 16 25

#10 20

#2 4 8 16

#output from for loops:

#1 4 9 16 25

#10 20

#2 4 6 8 10 12 14 16 18 20 22 24 26 28



