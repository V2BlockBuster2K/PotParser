from __future__ import print_function

import sys

from ..helpers import fix_float, is_float, mg_calculator
from ..utils.create_table import create_mg_info_table
from ..utils.help_printer import print_help


def percentage_menu() -> None:
    """Prompts the user to enter a percentage and calculates the number of milligrams of substance per gram."""
    while True:
        percentage = input(
            "Enter your percentage: ")
        if percentage.lower().strip() == 'back':
            return None
        elif percentage.lower().strip() == 'exit':
            sys.exit()
        elif percentage.lower().strip() == 'help':
            print_help()
        elif percentage.isdigit():
            dose = input(
                "Enter the dose you plan on consuming (in gram): ")
            if dose.lower().strip() == 'back':
                return None
            elif dose.lower().strip() == 'exit':
                sys.exit()
            elif dose.lower().strip() == 'help':
                print_help()
            elif is_float(dose):
                dose_fixed: float = fix_float(dose)
                mg: str = f"{mg_calculator(int(percentage), dose_fixed):9.2f}".strip()
                print(f"\n{dose_fixed}g contains {mg}mg")
                print(create_mg_info_table(int(percentage), dose_fixed))
            else:
                print(
                    "Invalid input. Please enter a number between 0 and 100, or type 'back', 'exit', or 'help'.")
        else:
            print(
                "Invalid input. Please enter a number between 0 and 100, or type 'back', 'exit', or 'help'.")
