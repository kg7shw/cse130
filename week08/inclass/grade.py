def display_grade(grade):
    """ Break a grade such as "A+" and "+" """

    # paranoia assert

    assert type(grade) == str
    assert len(grade) == 2 or len(grade) == 1
    assert grade(0) in ["A", "B", "C", "D", "F"] # Precondition
    if __debug__ and len(grade) == 2:
        assert grade[1] in ["+", "-"]

    letter = grade[0]
    sign = grade[1] if len(grade) == 2 else ""

    assert sign in ["+", "-", ""]
    assert letter in ["A", "B", "C", "D", "F"] # post condition

    print("Your letter grade is", letter, "and your sign is", sign)

display_grade("B+")