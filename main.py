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



def invite():
    """
    This function asks the number of people they want to invite and prints the guest list

    :return: Total guests 
    """
    while True:
        try:

            # Ask the user how many guests they want to invite
            total_guests = int(input("How many people would you like to invite? : "))
            
            add_guest(total_guests)
            break

        except ValueError:
            print("Please enter a valid integer")
            continue

    return total_guests

invite()

# Print out invitations for each dinner guest

# Ask the user if they want to replace someone

# Replace person if user chooses "y"

# Regenerate invitation list

# Add play again 