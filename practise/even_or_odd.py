def check_even_or_odd(number):
    """
    check number is even or odd.
    number (int): the number check
    return:
           None
    """

    # check the remainder after dividing the number by 2 is equal to zero.
    if number % 2 == 0:
    #f the remainder is zero, the number is even
        print(f"{number} is even")
    else:
        # If the remainder is not zero, the number is odd
        print(f"{number} is odd")