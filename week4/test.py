def main():
    color_group = input("Do you own all the green properties? (y/n) ")
    output = ""
    cash_requirement = 0

    if color_group.lower() == "y":
        pennsylvania_avenue = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        if pennsylvania_avenue != 5:
            north_carolina_avenue = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
            if north_carolina_avenue != 5:
                pacific_avenue = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
                if pacific_avenue != 5:
                    hotels = int(input("How many hotels are there to purchase? "))
                    if hotels >= 1:
                        houses = int(input("How many houses are there to purchase? "))
                        total_houses = pacific_avenue + north_carolina_avenue + pennsylvania_avenue
                        if houses >= total_houses:
                            cash_requirement = total_houses * 200
                            user_cash = int(input("How much cash do you have to spend? "))
                            if user_cash >= cash_requirement:
                                if north_carolina_avenue != 5 and pacific_avenue != 5:
                                    if north_carolina_avenue != 5 and pacific_avenue != 5:
                                        output = f"This will cost ${cash_requirement}. Purchase 1 hotel and {houses} house(s). Put 1 hotel on Pennsylvania and return any houses to the bank."
                                    else:
                                        output = f"This will cost ${cash_requirement}. Purchase 1 hotel and {houses} house(s). Put 1 hotel on Pennsylvania and return any houses to the bank. Put {houses} house(s) on Pacific."
                                else:
                                    output = f"This will cost ${cash_requirement}. Purchase 1 hotel and {houses} house(s). Put 1 hotel on Pennsylvania and return any houses to the bank. Put {houses} house(s) on North Carolina. Put {houses} house(s) on Pacific."
                            else:
                                output = "Out: Cash\n\nYou do not have sufficient funds to purchase a hotel at this time."
                        else:
                            output = "Out: No Houses\n\nThere are not enough houses available for purchase at this time."
                    else:
                        output = "Out: No Hotels\n\nThere are not enough hotels available for purchase at this time."
                else:
                    output = "Out: Swap PC\n\nSwap Pacific's hotel with Pennsylvania's 4 houses."
            else:
                output = "Out: Swap NC\n\nSwap North Carolina's hotel with Pennsylvania's 4 houses."
        else:
            output = "Out: One Hotel\n\nYou cannot purchase a hotel if the property already has one."
    else:
        output = "Out: No Properties\n\nYou cannot purchase a hotel until you own all the properties of a given color group."

    print(output)

if __name__ == "__main__":
    main()
