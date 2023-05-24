# Prompt: PC
pacific_avenue = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))

# Prompt: NC
north_carolina_avenue = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))

# Prompt: PA
pennsylvania_avenue = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))

# Prompt: Cash
cash = int(input("How much cash do you have to spend? "))

# Prompt: Houses
houses = int(input("How many houses are there to purchase? "))

# Prompt: Hotels
hotels = int(input("How many hotels are there to purchase? "))

# Prompt: Color Group
color_group = input("Do you own all the green properties? (y/n) ")

# Initialize output variable
output = ""

# Check conditions and generate output
if cash < 200:
    output = "Out: Cash\n\nYou do not have sufficient funds to purchase a hotel at this time."
elif houses < 4:
    output = "Out: No Houses\n\nThere are not enough houses available for purchase at this time."
elif hotels < 1:
    output = "Out: No Hotels\n\nThere are not enough hotels available for purchase at this time."
elif color_group == "n":
    output = "Out: No Properties\n\nYou cannot purchase a hotel until you own all the properties of a given color group."
elif pennsylvania_avenue == 5:
    output = "Out: One Hotel\n\nYou cannot purchase a hotel if the property already has one."
elif north_carolina_avenue == 5:
    output = "Out: Swap NC\n\nSwap North Carolina's hotel with Pennsylvania's 4 houses."
elif pacific_avenue == 5:
    output = "Out: Swap PC\n\nSwap Pacific's hotel with Pennsylvania's 4 houses."
else:
    price = 200
    total_houses = 4
    if hotels > 1:
        price += (hotels - 1) * 200
        total_houses += (hotels - 1) * 4

    output = f"Out: Purchase A\n\nThis will cost ${price}.\n" \
             f"Purchase 1 hotel and {total_houses} house(s).\n" \
             "Put 1 hotel on Pennsylvania and return any houses to the bank.\n" \
             f"Put {total_houses} house(s) on North Carolina.\n" \
             f"Put {total_houses} house(s) on Pacific."

print(output)
