'''
Test your function by:
Prompting the user for their birthday month,
birthday day-of-the-month, and birthday year
Calling your new function and saving the return string in a variable bDay
Printing the formatted birthday string
'''
from birthday import birthday
m = int(input("Please enter your birthday month:"))
d = int(input("Please enter your birthday day:"))
y = int(input("Please enter your birthday year:"))
formatted_BD = birthday(m, d, y)
print(formatted_BD)