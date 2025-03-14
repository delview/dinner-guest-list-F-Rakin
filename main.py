# F.Rakin_Dinner_Guest_List

# Create a program that will take user input about dinner guests they are inviting

def add_guest(total_guests : int , guest_list : list) -> str :
    """
    This function adds the names of the people invited to the guest list and sends a personalized invitation
    """
    # Track the number of guests in the list
    guest_counter = 1

    while True:
        try: 
            # If input is less than 0, tells user to invite atleast 1 guest
            if total_guests < 0:
                print("You need to invite atleast 1 person! ")

                # Runs the main function again for a different input
                invite()
                break

            # Create a loop that will keep appending names to the list until the maximum number is reached
            elif guest_counter <= total_guests:

                # Add names to a list
                new_guest = input("Invite a person to The Grand Banquet : ").title().strip()

                # Loop to check if new guest is already in the list
                if new_guest in guest_list:
                    print(f"\n{new_guest} is already invited to the Dinner!\n")  
                    continue

                # Add guest to list if already not in list
                else:
                    guest_list.append(new_guest)

                    guest_counter += 1
                    # Print a message saying that the guest has been added
                    print(f"\n{new_guest} has been added to the invitation list\n")
                    continue

            # Breaks loop when all guests are invited
            elif guest_counter > total_guests: 
                break

        except ValueError:
            # Continue the loop if invalid arguements are inputted
            print("Please enter valid arguements! ")
            continue


def print_list(name : str, guest_list : list) -> str:
    """
    This function prints the guest list with personalized invitations
    """
    # Print the total number of guests 
    print(f"\nTotal number of guests invited: {len(guest_list)}")

    # Print out invitations for each dinner guest
    for guest in guest_list:
        print(f"\nHello {guest}! \n\
You have been cordially invited to my Dinner. Please let me know if this Saturday night is a good time for you.  \n\
With regards \n\
{name} \n")


def edit_guest(name : str, guest_list : list) -> str:
    """
    This functions asks the user if they want to remove or add another guest to the list before printing the list
    """
    while True:
        try:
            print(" 1. Remove a guest from the list \n 2. Add another guest to the list \n 3. Print the invitation List \n 4. Exit the program")

            # Give user the options to edit the list 
            choice = int(input("Please choose an option [1/2/3/4] : "))

            if choice == 1:
                # Ask user for the name of a guest 
                removed_guest = input("Write the name of the person you want to remove : ").strip().title()

                # Remove the guest from the list
                guest_list.remove(removed_guest)
                
                # Print a message saying the guest is removed
                print(f"\n{removed_guest} has been removed from the invitation list\n")
                continue

            elif choice == 2:
                # Ask user for the name a guest
                added_guest = input("Invite another person to the Dinner: ").title().strip()

                # Loop again if the added guest is already in the list
                if added_guest in guest_list:
                    print(f"\n{added_guest} is already invited to the Dinner!\n")  
                    continue

                # Add guest to list if already not in list
                else:
                    guest_list.append(added_guest)

                    # Print a message saying that the guest has been added
                    print(f"\n{added_guest} has been added to the invitation list\n")
                    continue

            elif choice == 3: 
                # Regenerate invitation list
                print_list(name, guest_list)
                continue

            elif choice == 4:
                # End the program
                print("Thank you for using the Dinner Guest List")
                break

        except ValueError:
            print("Please enter a valid operation or accurate name of a guest!")
            continue


def invite() -> str:
    """
    This function greets the user and asks the number of people they want to invite and prints the guest list

    :return: Total guests 
    """
    # Start with an empty guest list
    guest_list = []

    user_name = input("What is your name? \n").title().strip() 

    print(f"Hi {user_name}! Welcome to the Guest List Organizer.") 

    while True:
        try:

            # Ask the user how many guests they want to invite
            total_guests = int(input("How many people would you like to invite? : "))
                
            # Call the function to add guests to the list
            add_guest(total_guests, guest_list)

            # Call the function to allow user to edit the list
            edit_guest(user_name, guest_list)
            
            break

        except ValueError:
            # Continue loop if invalid integer is inputted
            print("Please enter a valid integer")
            continue

  
# Call the main invite function to run the program
if __name__ == "__main__":  
    invite()