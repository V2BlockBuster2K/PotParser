from tabulate import tabulate
from ..helpers import mg_calculator

def create_strain_info_table(strain_name: str, strain_scraper_result) -> str:
    """
    Given a strain name and its web scraper results, create a table with the following headers:
    - Strain Name (formatted with titlecase and spaces instead of dashes)
    - Cannaconnection
    - Leafly
    - Wikileaf

    The table includes information about genetics, THC/CBD content, effects, and other attributes of the strain.

    Args:
    - strain_name: a string representing the name of the strain
    - strain_scraper_result: a list of 3 dictionaries, each containing information about the strain

    Returns:
    - A formatted string containing the table with the strain information

    Example usage:
    >>> result = create_strain_info_table("blue-dream", [{'Genetics': 'Sativa-dominant (70%)', 'THC': '19%', 'CBD': '0.1%', 'Effects': ['Motivated', 'Sociable', 'Cerebral'], 'Other': ['Berry', 'Sweet', 'Herbal', 'Pine']}, {'Genetics': 'Hybrid', 'THC': '18%', 'CBD': '0%', 'Effects': ['Creative', 'Uplifted', 'Energetic', 'Dry mouth', 'Paranoid', 'Dry eyes'], 'Other': ['Stress', 'Anxiety', 'Depression']}, {'Genetics': '60% Sativa', 'THC': '24%', 'CBD': '1%', 'Effects': ['Creative', 'Relaxed', 'Energetic'], 'Other': ['Afternoon']}])
    >>> print(result)
    ┌──────────────┬───────────────────────┬─────────────┬────────────────┐
    │ Blue Dream   │ Cannaconnection       │ Leafly      │ Wikileaf       │
    ├──────────────┼───────────────────────┼─────────────┼────────────────┤
    │ Genetics     │ Sativa-dominant (70%) │ Hybrid      │ 60% Sativa     │
    ├──────────────┼───────────────────────┼─────────────┼────────────────┤
    │ THC          │ 19%                   │ 18%         │ 24%            │
    ├──────────────┼───────────────────────┼─────────────┼────────────────┤
    │ CBD          │ 0.1%                  │ 0%          │ 1%             │
    ├──────────────┼───────────────────────┼─────────────┼────────────────┤
    │ Effects      │ Motivated             │ Creative    │ Creative       │
    │              │ Sociable              │ Uplifted    │ Relaxed        │
    │              │ Cerebral              │ Energetic   │ Energetic      │
    │              │                       │ Dry mouth   │                │
    │              │                       │ Paranoid    │                │
    │              │                       │ Dry eyes    │                │
    ├──────────────┼───────────────────────┼─────────────┼────────────────┤
    │ Other        │ Flavour:              │ Helps with: │ Best use time: │
    │              │ Berry                 │ Stress      │ Afternoon      │
    │              │ Sweet                 │ Anxiety     │                │
    │              │ Herbal                │ Depression  │                │
    │              │ Pine                  │             │                │
    └──────────────┴───────────────────────┴─────────────┴────────────────┘
    """
    # Join lists as strings in the dictionary
    for idx, values in enumerate(strain_scraper_result):
        for key, value in values.items():
            if isinstance(value, list):
                if idx == 0 and key == "Other":
                    values[key] = "Flavour:\n" + "\n".join(value)
                elif idx == 1 and key == "Other":
                    values[key] = "Helps with:\n" + "\n".join(value)
                elif idx == 2 and key == "Other":
                    values[key] = "Best use time:\n" + "\n".join(value)
                else:
                    values[key] = "\n".join(value)

    # Create the table from the dictionary
    headers = [strain_name.replace(
        "-", " ").title(), "Cannaconnection", "Leafly", "Wikileaf"]
    table = [[key]+[value.get(key) for value in strain_scraper_result]
             for key in ['Genetics', 'THC', 'CBD', 'Effects', 'Other']]
    return tabulate(table, headers=headers, tablefmt="simple_grid")


def create_mg_info_table(percentage: int, amount: float) -> str:
    """
    Generate a table of estimated THC levels and THC loss due to heating
    based on the input THC percentage and amount of marijuana inhaled.

    Args:
        percentage (int): The THC percentage of the marijuana being inhaled.
        amount (float, optional): The amount of marijuana being inhaled in grams.

    Returns:
        str: A formatted table displaying estimated THC levels and THC loss due to heating for different methods of consumption.
    """
    mg: float = mg_calculator(percentage, amount)

    # reference: https://www.latimes.com/projects/la-me-weed-101-thc-calculator/
    joint: float = mg * 0.36877076411960132890
    bong: float = mg * 0.39867109634551495017
    vaporizer: float = mg * 0.54152823920265780731

    headers = [f"THC: {percentage}%", "Estimated THC\ninhaled (mg)",
               "THC loss due\nto heating (mg)"]
    table = [["Joint", f"{joint:9.0f}", f"{mg-joint:9.0f}"],
             ["Bong", f"{bong:9.0f}", f"{mg-bong:9.0f}"], ["Vaporizer", f"{vaporizer:9.0f}", f"{mg-vaporizer:9.0f}"]]
    return tabulate(table, headers=headers, tablefmt="simple_grid")
