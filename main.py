# F.Rakin_Dinner_Guest_List

# Create a program that will take user input about dinner guests they are inviting

def add_guest(total_guests : int , guest_list : list) -> str :
    """
    This function adds the names of the people invited to the guest list and sends a personalized invitation
    """
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



def edit_guest(name, guest_list):
    """
    This functions asks the user if they want to remove or add another guest to the list
    """
    while True:
        try:
            print(" 1. Remove guest \n 2. Add guest \n 3. Print List \n 4. Exit")

            choice = int(input("Please choose an option [1/2/3/4] : "))

            if choice == 1:
                guest_list.remove(input("Write the name of the person you want to remove : "))

                continue

            elif choice == 2:
                guest_list.append(input("Invite another person to the Dinner: "))

                continue

            elif choice == 3: 
                print_list(name, guest_list)
                continue

            elif choice == 4:
                break

        except ValueError:
            print("Please enter a valid operation!")
            continue


def print_list(name, guest_list):
    """
    This function prints the guest list with personalized invitations
    """

    for guest in guest_list:
        print(f"Hello {guest}! \n\
You have been cordially invited to my Dinner. Please let me know if this Saturday night is a good time for you.  \n\
With regards \n\
{name}")

# Print out invitations for each dinner guest

# Ask the user if they want to replace someone

# Replace person if user chooses "y"

# Regenerate invitation list

def invite():
    """
    This function greets the user and asks the number of people they want to invite and prints the guest list

    :return: Total guests 
    """

    guest_list = []

    user_name = input("What is your name? \n").title().strip() 

    print(f"Hi {user_name}! Welcome to the Guest List Organizer.") 

    while True:
        try:

            # Ask the user how many guests they want to invite
            total_guests = int(input("How many people would you like to invite? : "))
                
            add_guest(total_guests, guest_list)
            edit_guest(user_name, guest_list)
            
            break

        except ValueError:
            print("Please enter a valid integer")
            continue

    return guest_list

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
        

invite()