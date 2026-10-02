import csv

gdp_2020 = {}

with open("World_GDPperCapita2020-2022.csv", "r") as file:
    header = file.readline()

    for row in file:
        if not row.strip():
            continue
        row = row.strip().split(",")

        if len(row) < 2:
            continue
        if row[1] == "The":
            country = row[0] + ", The"
            value_2020 = row[2]
        else:
            country = row[0]
            value_2020 = row[2]


        if value_2020 == "" or value_2020 == "..":
            gdp_2020[country] = None
        else:
            gdp_2020[country] = float(value_2020)


while True:
    country = input("Enter a country name (or type quit to quit):\n")

    if country.lower() == "quit":
        break

    if country in gdp_2020:
        if gdp_2020[country] is None:
            print("The data is missing for 2020")
        else:
            print(f"In 2020, the GDP per capita, PPP (in current international $) was $ {gdp_2020[country]:,.2f}")
    else:
        print("Country not found")