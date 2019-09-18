def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]

def squares_by_loop(number):
    """ Creates a  list of squares of numbers for each number that when divided by 3 has 1 as the remainder.
        For all the numbers from 0 to the number-1. Returns list with the appropriate numbers.
    """
    list_of_numbers = []
    for tall in range(number):
        if tall % 3 == 1:
            list_of_numbers.append(tall)

    return list_of_numbers
