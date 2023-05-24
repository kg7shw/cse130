# Sources:

# https://docs.python.org/3/library/functions.html#max

# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      Write a program to inform the user if he or she is able to build
#      a hotel on Pennsylvania Avenue. This program will ask the user
#      several questions and, based on these questions, tell the user whether 
#      a hotel can be purchased for Pennsylvania and how much it will cost.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was making the solution more efficient and more
#      human readable. I found it hard to make my code readable to even
#      myself so how could I expect someone else to be able to read it.
#      It wasn't hard creating the program since I had a design to work
#      on and the design was good enough that writning the code off of
#      the flowchart was pretty easy.
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-




output = ""
total_money_need = 0

def main():
    # Prompt: Color Group
    color_group = input("Do you own all the green properties? (y/n) ")

    if color_group.lower() == "y":
        # Prompt: PA
        pennsylvania_avenue = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        if pennsylvania_avenue != 5:
            # Prompt: NC
            north_carolina_avenue = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
            if north_carolina_avenue != 5:
                # Prompt: PC
                pacific_avenue = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
                if pacific_avenue != 5:
                    # Prompt: Hotels
                    hotels = int(input("How many hotels are there to purchase? "))
                    if hotels >= 1:
                        # Prompt: Houses
                        houses = int(input("How many houses are there to purchase? "))
                        number_houses = (pacific_avenue + north_carolina_avenue + pacific_avenue)
                        if houses >= number_houses:
                            total_money_need = (number_houses) * 200

                            # Calculate: number_houses_PA_need
                            # Calculate: number_houses_NC_need
                            # Calculate: number_houses_PC_need
                            # Calculate: number_houses_total_need
                            # Calculate: total_money_need


                            # Prompt: Cash
                            user_cash = int(input("How much cash do you have to spend? "))
                            if user_cash >= total_money_need:
                                if north_carolina_avenue != 5 and pacific_avenue != 5:
                                    if north_carolina_avenue != 5:
                                        if pacific_avenue != 5:
                                            # Out: Purchase D
                                            output = f"This will cost ${total_money_need}. Purchase 1 hotel and {number_houses} house(s).Put 1 hotel on Pennsylvania and return any houses to the bank."

                                        else:
                                            # Out: Purchase C
                                            output = f"This will cost ${total_money_need}. Purchase 1 hotel and {number_houses} house(s).Put 1 hotel on Pennsylvania and return any houses to the bank. Put {number_houses} house(s) on Pacific."


                                    else:
                                        # Out: Purchase B
                                        output = f"This will cost ${total_money_need}.Purchase 1 hotel and {number_houses} house(s). Put 1 hotel on Pennsylvania and return any houses to the bank. Put {number_houses} house(s) on North Carolina."

                                else:
                                    # Out: Purchase A
                                    output = f"This will cost ${total_money_need}. Purchase 1 hotel and {number_houses} house(s). Put 1 hotel on Pennsylvania and return any houses to the bank. Put {number_houses} house(s) on North Carolina. Put {number_houses} house(s) on Pacific."
                            else:
                                # Out: Cash
                                output = "Out: Cash\n\nYou do not have sufficient funds to purchase a hotel at this time."
                        else:
                            # Out: No Houses
                            output = "Out: No Houses\n\nThere are not enough houses available for purchase at this time."
                    else:
                        # Out: No Hotels
                        output = "Out: No Hotels\n\nThere are not enough hotels available for purchase at this time."
                else:
                    # Out: Swap PC
                    output = "Out: Swap PC\n\nSwap Pacific's hotel with Pennsylvania's 4 houses."
            else:
                # Out: Swap NC
                output = "Out: Swap NC\n\nSwap North Carolina's hotel with Pennsylvania's 4 houses."

        else:
            # Out: One Hotel
            output = "Out: One Hotel\n\nYou cannot purchase a hotel if the property already has one."

    else:
        # Out: No Properties
        output = "Out: No Properties\n\nYou cannot purchase a hotel until you own all the properties of a given color group."

    return print(output)
    




if __name__ == "__main__":
    main()

#     Out: Purchase A

# This will cost ${total_money_need}.
#          Purchase 1 hotel and {number_houses} house(s).
#          Put 1 hotel on Pennsylvania and return any houses to the bank.
#          Put {number_houses} house(s) on North Carolina.
#          Put {number_houses} house(s) on Pacific.
# Out: Purchase B

# This will cost ${total_money_need}.
#          Purchase 1 hotel and {number_houses} house(s).
#          Put 1 hotel on Pennsylvania and return any houses to the bank.
#          Put {number_houses} house(s) on North Carolina.
# Out: Purchase C

# This will cost ${total_money_need}.
#          Purchase 1 hotel and {number_houses} house(s).
#          Put 1 hotel on Pennsylvania and return any houses to the bank.
#          Put {number_houses} house(s) on Pacific.
# Out: Purchase D

# This will cost ${total_money_need}.
#          Purchase 1 hotel and {number_houses} house(s).
#          Put 1 hotel on Pennsylvania and return any houses to the bank.