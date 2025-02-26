# Practice for main project

guest_list = []

guests = 1

counter = 1

while True:
    
    if guests <= 2:
        guest_list.append(input("Invite a person to The Grand Banquet? : ").title().strip())
        guests += 1
        continue

    elif guests > 2: 
        break

# Make a list that includes these people and use the list to generate a personalized message to each person, inviting them to dinner.

guest_list.sort()

print(f"You have invited {len(guest_list)} people to The Grand Banquet ")

for guest in guest_list:
    print(f"Hi {guest}! You have graciously been invited to The Grand Banquet!")

remove_guest = int(input("Please enter the number of the guest you want to replace: "))


guest_list[remove_guest - 1] = input("Who do you want to replace the person with? : ").strip().capitalize()

print(guest_list)