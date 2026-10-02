# setting variables

meters = float(input("Enter the distance in meters: "))


mi_convert = 1609.344                                           # getting variables ready for arithmetic setting values
ft_convert = 3.28084
inch_convert = 39.3700787402


len_miles = meters / mi_convert                                 # creating the proper conversions
len_feet = meters * ft_convert
len_inches = meters * inch_convert


miles = round(len_miles, 2)                                     # setting the outputs to round by two decimal points
feet = round(len_feet, 2)
inches = round(len_inches, 2)


print(meters, "meters is", miles, "miles")                      # printing the proper outputs
print(meters, "meters in feet is ", feet , "feet")
print(meters, "meters in inches is ", inches, "inches")


