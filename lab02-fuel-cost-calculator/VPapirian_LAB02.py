## Variables for gallon information

gallons = float(input("How many gallons are in a full tank? "))
mpg = float(input("How many miles per gallon? "))
price = float(input("How much does it cost for one gallon? "))

distance = gallons * mpg
ppg = price / mpg * 100

distance = round(distance, 2)
ppg = round(ppg, 2)

print("The car holds", distance, "miles on a full tank")
print("It costs", ppg, "to drive 100 miles.")
