def compute_tax(income):

    brackets = [
        (0, 15100, 0, 0.10)
        (15100, 61300, 8440, 0.15)
        (61300, 61300, 8440, 0.25)
        (123400, 61300, 24040, 0.28)
        (188450, 61300, 42170, 0.33)
        (15100, 61300, 914043, 0.35)
 ]


    for bracket in brackets:
        if bracket[0] <= income <= bracket[1]:
            return bracket[2] + bracket[3] * (income - bracket[0])
    
    return 0.0



