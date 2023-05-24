


def property_function():
    output = ""
    total_money_need = 0

    # Prompt: Color Group
    color_group = input("Do you own all the green properties? (y/n) ")

    if color_group.lower() != "y":
        output = "Out: No Properties\n\nYou cannot purchase a hotel until you own all the properties of a given color group."
        return output

    # Prompt: PA
    pennsylvania_avenue = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    if pennsylvania_avenue == 5:
        output = "Out: One Hotel\n\nYou cannot purchase a hotel if the property already has one."
        return output

    # Prompt: NC
    north_carolina_avenue = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    if north_carolina_avenue == 5:
        output = "Out: Swap NC\n\nSwap North Carolina's hotel with Pennsylvania's 4 houses."
        return output

    # Prompt: PC
    pacific_avenue = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    if pacific_avenue == 5:
        output = "Out: Swap PC\n\nSwap Pacific's hotel with Pennsylvania's 4 houses."
        return output

    # Prompt: Hotels
    hotels = int(input("How many hotels are there to purchase? "))
    if hotels < 1:
        output = "Out: No Hotels\n\nThere are not enough hotels available for purchase at this time."
        return output

    # Prompt: Houses
    houses = int(input("How many houses are there to purchase? "))
    number_houses = (pacific_avenue + north_carolina_avenue + pacific_avenue)
    if houses < number_houses:
        output = "Out: No Houses\n\nThere are not enough houses available for purchase at this time."
        return output

    # Calculate houses on Pennsylvania Avenue, North Carolina Avenue, Pacific Avenue.
    number_houses_PA = 5 - pennsylvania_avenue
    number_houses_NC = 5 - north_carolina_avenue
    number_houses_PC = 5 - pacific_avenue
    # Calculate total houses
    number_houses_total_need = number_houses_PA + number_houses_NC + number_houses_PC
    # Calculate the total money needed.
    total_money_need = number_houses_total_need * 200

    # Prompt: Cash
    user_cash = int(input("How much cash do you have to spend? "))
    if user_cash < total_money_need:
        output = "Out: Cash\n\nYou do not have sufficient funds to purchase a hotel at this time."
        return output

    if north_carolina_avenue != 5 and pacific_avenue != 5:
        output = f"This will cost ${total_money_need}. Purchase 1 hotel and {number_houses} house(s). Put 1 hotel on Pennsylvania and return any houses to the bank."
        return output

    if north_carolina_avenue != 5:
        output = f"This will cost ${total_money_need}. Purchase 1 hotel and {number_houses} house(s). Put 1 hotel on Pennsylvania and return any houses to the bank. Put {number_houses} house(s) on Pacific."
        return output

    if pacific_avenue != 5:

        output = f"This will cost ${total_money_need}. Purchase 1 hotel and {number_houses} house(s). Put 1 hotel on Pennsylvania and return any houses to the bank. Put {number_houses} house(s) on North Carolina. Put {number_houses} house(s) on Pacific."
        return output

def main():
    output = property_function()
    print(output)

if __name__ == "__main__":
    main()