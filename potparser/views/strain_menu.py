from __future__ import print_function

import asyncio
import sys

from ..helpers import create_url_ending_name
from ..utils import create_strain_info_table, print_help
from ..webscrapers import scrape_strain_info


def strain_menu() -> None:
    """Prompts the user to enter a strain name and fetches information about that strain."""
    while True:
        strain_name = input("Enter your strain name: ")
        if strain_name.lower().strip() == 'exit':
            sys.exit()
        elif strain_name.lower().strip() == 'back':
            return None
        elif strain_name.lower().strip() == 'help':
            print_help()
        else:
            if strain_name.strip() != '':
                url_ending_name = create_url_ending_name(strain_name)
                result = asyncio.run(scrape_strain_info(url_ending_name))
                table = create_strain_info_table(result, strain_name)
                print(table)
    else:
        print(
            "Invalid input. Please enter a Strain, or type 'back', 'exit', or 'help'.")
