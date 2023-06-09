def linear_search(array, search):
    """Return True if 'search' exists in 'array'"""

    # Paranoid checks to make sure the input is valid
    if __debug__:
        assert type(array) == type([])
        assert len(array) >= 0
        assert len(array) == type(0)
        for element in array:
            assert type(element) == type(search) # this is placed right

    # Look at every element in the array, from the first tpo the last.
    for index in range(0, len(array)):

        # assert type(array[index]) == type(search) this is not placed right

        assert 0 <= index < len(array) # Always do this. This helps with catching index out of range errors. Always assert your indicies
        


        # Compare every element with the search term.
        if array[index] == search:
            return True
        
    # If we made it all the way to the end without finding it, it is not there!
    return False