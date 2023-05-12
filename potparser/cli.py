from __future__ import print_function

import sys

from .utils import print_help
from .views.percentage_menu import percentage_menu
from .views.strain_menu import strain_menu


def handle_user_input(choice: str) -> bool:
    """
    Handles the user's input and executes the corresponding functionality based on the choice.

    Args:
        choice (str): The user's input.

    Returns:
        bool: True if the user input was valid and the corresponding functionality executed; False otherwise.
    """
    if choice.strip() == "1":
        strain_menu()
    elif choice.strip() == "2":
        percentage_menu()
    elif choice.lower().strip() == 'help':
        print_help()
    elif choice.lower().strip() == 'exit':
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
    return True


def main_menu() -> None:
    """
    Displays the main menu for the program and handles user input.

    The function creates a new asyncio event loop, and displays the menu options to the user.
    If the user selects option 1 or 2, it calls the `handle_user_input()` function to handle the input.
    If the user types 'help', the function displays the available commands.
    If the user types 'exit', the program terminates.
    If the user types any other input, the function prints an error message and displays the menu options again.

    Returns:
        None
    """
    while True:
        print("[1] Fetch strain percentage\n[2] Calculate mg based on percentage")
        choice = input("Enter your choice (1-2): ")
        if choice.isdigit() and int(choice) <= 2:
            back_to_menu = handle_user_input(choice)
            if not back_to_menu:
                continue
        elif choice.lower().strip() == 'help':
            print_help()
        elif choice.lower().strip() == 'exit':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


def main():
    main_menu()


if __name__ == '__main__':
    main()
