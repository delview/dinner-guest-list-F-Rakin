# F.Rakin_Dinner_Guest_List

# Create a program that will take user input about dinner guests they are inviting
import random

# Ask for user's name and greet them
def greeting() -> str :
    """
    This function asks the user's name and greets the user
    """
    name = input("What is your name? \n").title().strip()

    print(f"Hi {name}! Welcome to my Number Guessing Game.") 

    return name

def add_guest(total_guests : int) -> str :
    """
    This function adds the names of the people invited to the guest list
    """
    guest_list = []
    guest_counter = 1

    while True:
        try: 

            # Create a loop that will keep appending names to the list until the maximum number is reached
            if guest_counter <= total_guests:

                # Add names to a list
                guest_list.append(input("Invite a person to The Grand Banquet : ").title().strip())
                guest_counter += 1
                continue

            elif guest_counter > total_guests: 
                break

        except ValueError:
            print("Please enter valid arguements! ")
            continue

        return guest_list


def print_list(name, guest_list):
    """
    This function prints the guest list with personalized invitations
    """

    for guest in guest_list:
        print(f"Hello {guest}! \n\n\
        You have been cordially invited to my Dinner. Please let me know if this Saturday night is a good time for you. \n \n\
        With regards \n\
        {name}")


def invite():
    """
    This function asks the number of people they want to invite and prints the guest list

    :return: Total guests 
    """
    while True:
        try:

            # Ask the user how many guests they want to invite
            total_guests = int(input("How many people would you like to invite? : "))
            greeting()
            add_guest(total_guests)
            print_list(name, guest_list)
            
            break

        except ValueError:
            print("Please enter a valid integer")
            continue

    return total_guests

def replace_guest(guest_list):
    """
    This functions asks the user if they want to remove or replace a guest from the list
    """
    while True:
        try:
            print("1. Replace guest \n 2. Remove guest 3. Keep list same")

            choice = int(input("Please choose an option [1/2/3] : "))

            if choice == 1:
                
                continue

            elif choice == 2:

                continue

            elif choice == 3: 

                break

        except ValueError:
            print



# Print out invitations for each dinner guest

# Ask the user if they want to replace someone

# Replace person if user chooses "y"

# Regenerate invitation list

# Add use again 
def use_again() -> str:
    """
    This function gives the user the choice to use the program again.
    """
    while True:

        # Ask if they want to use the program again, only accepting 'y' or 'n'
        choice = input("Do you wish to use the guest list again? [y/n] - ").strip().lower()

        # Run game function again if user chooses "y"
        if choice == "y":
            invite()

        # End the game if user chooses "n"    
        elif choice == "n":
            break

        # Tell user to choose only between "y/n"
        else:
            print("Please enter y/n ") 
        

