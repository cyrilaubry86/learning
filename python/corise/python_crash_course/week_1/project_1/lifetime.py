

def calculate_lifetime_supply(current_age, amount_per_day):
    """ Returns the amount of items consumed over a lifetime
    (with a max age of 100 assumed) based on the current age
    and the amount consumed per day.

    >>> calculate_lifetime_supply(99, 1)
    365
    >>> calculate_lifetime_supply(99, 2)
    730
    >>> calculate_lifetime_supply(36, 3)
    70080
    """
    days_left = (100 - current_age) * 365
    return days_left * amount_per_day



