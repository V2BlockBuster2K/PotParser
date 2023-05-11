def create_url_ending_name(strain_name: str) -> str:
    """
    Creates a URL ending name for a given strain name by stripping leading and trailing whitespaces,
    converting the string to lowercase, and replacing internal spaces with hyphens.

    Args:
        strain_name (str): The name of the strain to create a URL ending name for.

    Returns:
        str: The URL ending name created from the strain name.
    """
    return strain_name.strip().lower().replace(" ", "-")
