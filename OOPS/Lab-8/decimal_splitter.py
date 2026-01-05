class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    def get_fraction(number):
        return number - int(number)

    """
    Method to check if a given number is odd or even
    """
    def is_odd(number):
        whole_part = int(number)
        return whole_part % 2 != 0
