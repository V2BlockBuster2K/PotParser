def mg_calculator(percentage: int, dose: float) -> float:
    """
    Calculate the number of milligrams (mg) in a dose based on the percentage and dose provided.

    Args:
        percentage (int): The percentage of the substance in the dose (e.g. 20 for 20%).
        dose (float): The amount of the substance in the dose (e.g. 0.5 for 0.5 grams).

    Returns:
        float: The number of milligrams in the dose calculated as percentage * 10 * dose.
    """
    mg = percentage * 10 * dose
    return mg