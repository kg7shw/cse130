def average_gpa(gpas):
    """Find the average GPA from the list"""

    # Preflight list checks to make sure my data is not wonky
    assert type(gpas) == type([]) # this better be a list
    assert len(gpas) > 0

    if __debug__:
        for gpa in gpas:
            assert type(gpa) == type(4.0) # Better be a number
            assert 0 <= gpa <= 4.0 # Better be a valid number

    #add them up

    sum = 0
    for gpa in gpas:
        sum += gpa
    #compute the average and returen.

    average = sum / len(gpas)
    assert 0 <= average <= 4.0 # The average better be a valid GPA as well.
    return average
