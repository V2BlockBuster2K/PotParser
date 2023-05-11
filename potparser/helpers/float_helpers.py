def is_float(num: str) -> bool:
    """
    Returns True if the given argument can be converted to a floating-point number, and False otherwise.

    Parameters:
    num (str): A string representing a number.

    Returns:
    bool: True if the input string can be converted to a float, False otherwise.
    """
    try:
        float(num)
        return True
    except ValueError:
        return False

def fix_float(num: str) -> float:
    """
    Takes a string and converts it to a float, fixing case where a '.' is at the beginning of the string.
    If the '.' is at the beginning of the string, a 0 is added before it.
    """
    if num.startswith('.'):
        num = '0' + num
    return float(num)