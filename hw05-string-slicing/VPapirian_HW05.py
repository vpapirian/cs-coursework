name = input("What is your name? ")

print("Full name:", name.upper())

space_index = name.find(" ")

last_name = name[space_index + 1:]
print("Last name:", last_name)

first_name = name[:space_index]
print("First name length:", len(first_name))