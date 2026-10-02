car_type = input("Do you have an electric car? ").upper()

distance = float(input("How far would you like to travel (in miles)?) "))

if car_type == "YES":
    range_full = float(input("What is the range of your car when fully charged (in miles)? "))
    charge_price = float(input("What is the average price (in $) to charge your car when you still have 50 miles of range remaining? "))

    cost = (distance / range_full) * charge_price
    print(f"It will cost you ${cost:.2f}.")

else:
    mpg = float(input("What is the fuel efficiency (miles per gallon) of your car? "))
    ppg = float(input("What is the average price per gallon (in $)? "))

    gas_cost = (distance / mpg) * ppg
    print(f"It will cost you ${gas_cost:.2f}.")