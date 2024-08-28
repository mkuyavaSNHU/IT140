# Marisa Kuyava

# A dictionary linking a room to other rooms and linking one item for each room
# except the Start room (Kitchen) and the room containing the villain (Pantry)
rooms = {
    'Kitchen': {'South': 'Office', 'North': 'Living Room', 'East': 'Dining Room', 'West': 'Master Bedroom',
                'item': 'None'},
    'Living Room': {'South': 'Kitchen', 'East': 'Den', 'item': 'Ball'},
    'Den': {'West': 'Living Room', 'item': 'Tug Rope'},
    'Master Bedroom': {'East': 'Kitchen', 'item': 'Blanket'},
    'Office': {'North': 'Kitchen', 'East': 'Guest Room', 'item': 'Mr Toucan'},
    'Guest Room': {'West': 'Office', 'item': 'Ms Unicorn'},
    'Dining Room': {'North': 'Pantry', 'West': 'Kitchen', 'item': 'Chew Stick'},
    'Pantry': {'South': 'Dining Room', 'item': 'Vacuum'}  # Villain Room
}

# list variable to hold inventory items that have been picked up
inventory = []

# current_room = 'Kitchen'
user_input = None


# Function to update room based on current_room and direction input from user - Returns updated room
def get_new_room(current_room, direction):
    new_room = None
    direction = direction.title()
    for r in rooms:  # For each room in rooms dictionary
        if r == current_room:  # If the room is equal to the players current_room
            if direction in rooms[r]:  # If room has direction
                new_room = rooms[r][direction]  # new room is set to room matching direction key value
    return new_room


# Function to add Item to inventory list
def get_item(current_room):
    inventory.append(rooms[current_room]['item'])  # Adds item to inventory list.
    del rooms[current_room][
        'item']  # Removes item from Rooms dictionary so that it no longer appears as an item to pick up.


# Function to provide game movement instructions
def show_instruct():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Instructions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Welcome to the Puppy Text Adventure Game')
    print('You are a small dog named Pixie and you just moved into your new house.')
    print('Your humans have been unpacking and all your favorite toys have been scattered throughout the room.')
    print('You have learned that there is an evil vacuum monster that is roaming the house.')
    print('To help you defeat the vacuum you need to gather some of your favorite things.')
    print("To win search the house and collect 6 Items before encountering the vacuum")
    print("Defeat is imminent if you find the vacuum before the items.")
    print('\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Commands~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Movement: 'go North', 'go South', 'go West', 'go East'")
    print("Add Item to Inventory: 'get 'itemName''")
    print('\n')


# Function to display current game status
def show_status():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Current Status~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You are in the ' + current_room)  # Prints current_room
    available_moves = rooms[current_room].keys()  # Gets directions (keys) that are available for exit from current room
    print('Directions available to move: ')
    for i in available_moves:  # Prints what directions are available to move for the current room
        if i != 'item':  # Keeps the KEY 'item' from printing
            print(i, end=', ')  # Prints all on the same line separated by a comma
    print()
    item = str(rooms[current_room].get('item'))  # Gets Item from Rooms dictionary and stores in variable
    print('Items available for pickup: ' + item)  # Prints Item that is available for pick in the current room
    print("Current Inventory: ")  # Prints Items that are currently stored in the inventory list
    for x in range(len(inventory)):
        print(inventory[x])
    print('Please enter a command:')


# Function to validate input and handle invalid input
def validate_user_input():
    while True:
        try:
            user_input_a, user_input_b = input().split(' ', 1)  # Splits user input and stores in 2 variables
            if user_input_a.lower() == 'go':  # Enters If statements if the first word in the user input is 'go'
                user_input_b = user_input_b.title()  # Sets user_input to title case to match dictionary items
                while user_input_b.title() not in rooms[
                    current_room].keys():  # Runs while user_input does not match any keys
                    print('This room does not have an exit in that direction or the input is invalid.')
                    show_status()  # Show status to give user what commands are available
                    user_input_a, user_input_b = input().split(' ', 1)
                    user_input_b = user_input_b.title()  # Sets user_input to title case to match dictionary items
                return user_input_a, user_input_b
            elif user_input_a.lower() == 'get':  # Enters If statements if the first word in the user input is 'get'
                user_input_b = user_input_b.title()  # Sets user_input to title case to match dictionary items
                while user_input_b.title() not in rooms[current_room].get(
                        'item'):  # Runs while user_input doesn't match keys
                    print('There is not an item in this room with that name or the input is invalid.')
                    show_status()  # Show status to give user what commands are available
                    user_input_a, user_input_b = input().split(' ', 1)
                    user_input_b = user_input_b.title()  # Sets user_input to title case to match dictionary items
                return user_input_a, user_input_b
        except ValueError as ve:
            print("That is not a valid command. Please try again.")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Commands~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("Movement: 'go North', 'go South', 'go West', 'go East'")
            print("Add Item to Inventory: 'get 'itemName''")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


show_instruct()
current_room = 'Kitchen'  # Set current room to starting room 'Kitchen'
# While loop that will continue as long as current_room is NOT 'Pantry'
while current_room != 'Pantry':
    show_status()  # Function call to show status
    user_input_a, user_input_b = validate_user_input()  # Function call to validate user_input
    if user_input_a.lower() == 'go':
        current_room = get_new_room(current_room, user_input_b)  # Function call to set current_room to new_room
    elif user_input_a.lower() == 'get':
        get_item(current_room)  # Function call to add Item to inventory

# While loop that will run when current_room is 'Pantry'
while current_room == 'Pantry':
    if len(inventory) == 6:  # Checks to see if inventory length matches number of items required to win
        print('You have successfully collected all items and are ready to face the vacuum.')
        print('You quickly eat the CHEW STICK to give you energy.')
        print('You hide under the BLANKET and roll the BALL across the floor')
        print('to create a distraction while MR. TOUCAN and MS. UNICORN sneak up behind.')
        print('With everything in place you charge the vacuum with the TUG ROPE.')
        print('The rope quickly gets tangled in the vacuum, rendering it helpless.')
        print('CONGRATULATIONS! You have defeated the evil vacuum!')
        quit()
    else:
        print(
            'You enter the pantry, realizing to late that you do not have all of the items needed to defeat the vacuum.')
        print('You quickly turn and run, knowing that you are defeated. Maybe next time....')
        quit()
