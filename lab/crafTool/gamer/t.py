'''
NAME: John Cook
DESC:  In the Foyer there are the shoesOfHermes,
        these shoes have wings giving the user flight and speed.
        In the WashRoom there is a elementalWand, this lets you summon
        different elements blast depending on the season. In the
         CrystalBallSurveillance room you will find a crystalBall,
        there are 8 crystal balls on for each room then one that you
        can carry around to watch the rooms from anywhere but you
        cannot see the portal room from them. Kitchen this is where
        the food for the beast is SaltCuredMeat this should be
        zapped with the wand. Last in the WineCellar this is where
        the Potion is and should be taken if bitten by the Wendigo.
1. You must retrieve all 6 items aboard the ship.
2. You must turn on the engine room's power.
3. You must defeat the zombie once all 6 items have been collected.
'''


### Dictionaries ###


# Move will change player position towards room
rooms = {
    'WashRoom': {'West': 'Foyer', 'item': 'Elemental Wand'},
    'Foyer': {'North': 'Temple', 'East': 'Washroom', 'item': 'Shoes of Hermes'},
    'Temple': {'South': 'Foyer', 'North': 'Kitchen', 'West': 'Crystal Ball Surveillance Room', 'item': 'Samurai Armor'},
    'Crystal Ball Surveillance Room': {'East': 'Temple', 'item': 'Crystal ball'},
    'Kitchen': {'South': 'Temple', 'East': 'Food Storage', 'item': 'Salt Cured Meat'},
    'Wine Cellar': {'South': 'Unknown Portal', 'item': 'Potion'},
    'Unknown Portal': {'North': 'Wine Celler', 'item': 'Wendigo'}
}

# Use will change room
# 1 = True. 0 = False. True means there is nothing else to use in the room"
# Values must add up to 8 to win the game
room_function = {
    'WashRoom': 1,
    'Foyer': 1,
    'Temple': 1,
    'Crystal Ball Serveillance Room': 1,
    'Kitchen': 1,
    'Wine Cellar': 1,
    'Unknown Portal': 1
}

# Inspect will retrieve items if they are set to FREE. If RESTRICTED is set, need another item to get.
collectibles = {
    'WashRoom': { 'Elemental Wand': 'FREE'},
    'Foyer': {'Shoes of Hermes': 'FREE'},
    'Temple': {'Samurai Armor': 'FREE'},
    'Crystal Ball Surveillance Room': {'Crystal ball': 'FREE'},
    'Kitchen': {'Salt Cured Meat': 'FREE'},
    'Wine Cellar': {'Potion': 'FREE'}
}

# Description of rooms to be used if condition is not fulfilled (Inspect)
room_desc = {
    'WashRoom': 'This is a nice bathroom but why are there so many mirrors',
    'Foyer': 'You see a sign that ask you to remove your shoes',
    'Temple': 'Just a open and empty room with a burn pit in the middle looks like it was used recently',
    'Crystal Ball Surveillance Room': 'Why do they work like ring cameras lol ',
    'Kitchen': 'Smells a lil musky must be the broccoli',
    'Wine Cellar': 'Grab some wine or look for the ',
    'Unknown Portal': 'This is when you realize that stench wasn\'t the broccoli'
}

# Description of rooms to be changed once respective conditions have been fulfilled
room_desc_update = {
    'WashRoom': 'This is a nice bathroom but really creapy',
    'Foyer': 'Still can\'t find that damn cat',
    'Temple': 'kitty kitty ',
    'Crystal Ball Surveillance Room': 'Why do they work like ring cameras lol ',
    'Kitchen': 'Smells a lil musky must be the broccoli',
    'Wine Cellar': 'Grab some wine or look for the ',
    'Unknown Portal': 'this isn\'t going to be fun'
}


### Global Variables ###


current_room = "Foyer"
move_counter = 0  # Total moves in the game.
item_counter = 0  # How many total items have been retrieved
room_counter = 0  # How many rooms are fully functional
fixed_engine_room = False
quit_game = False
inventory = []


### General Game Functions ###


# The first function to be displayed.
def WelcomeMessage():
    print("\n<<-=========================================================->>\n")
    print('               Portal Protector           \n'
          '     You have picked up a summer job temple \n'
          '     sitting at the mountain temple for your \n'
          '     local wizard and for some reason you cannot \n'
          '     find his pet cat. In order to find the cat \n'
          '     you go to the wizards crystal surveillance \n'
          '     room and realize that the cat isn’t in the \n'
          '     Foyer, washroom, main temple so then when \n'
          '     you check the kitchen, food storage still no cat. \n'
          '     While checking the wine celler you realize that the \n'
          '     cat has made its way into the portal room. So now you \n'
          '     must rescue the cat from the portal but beware because \n'
          '     it leads to a realm that is protected by a hungry Wendigo.')
    print("\n<<-===============================================================->>\n")

# A function that provides players with a list of options
def HelpMessage():
    print("<< List of commands to type >>")
    print("'Move': Choose to move either north, south, east, or west.")
    print("'Use': Use an item in a certain room")
    print("'Inspect': Examine the room for items")
    print("'Map': Examine the layout of the ship!")
    print("'Exit': Ends the game")

# Display map through ASCII art!
def DisplayMap():
    # 40 lines of whitespace
    print("                                                                              \n"
          "                _________        _______________               ^ North        \n"
          "               | Kitchen | ---> | Food Storage  |                             \n"
          "               |_______  | <--- |__________| |__|                             \n"
          "                       | |                 | |                                \n"
          " ______________     ___| |___           ___| |____________                    \n"
          " | C.Ball Room |<-  |        |          |   Wine Celler  |                    \n"
          " |_____________| -> | Temple |          |____________  __|                    \n"
          "   ----------       |__//____|                       | |                      \n"
          "                      //                             / /                      \n"
          "                     //                             / /                       \n"
          "                ____//__       __________        __| |_***************__      \n"
          "               |  Foyer | --> | Washroom |       |   Unknown Portal   |       \n"
          "               |________| <-- |__________|       |____________________|       \n"
        )

# The menu that shows up after every action, displaying the player's status.
def Menu():
    global current_room
    global item_counter
    global quit_game

    item_counter = len(inventory)

    print("\n< ================================================================================================== >")
    print("You are currently in:", current_room)
    print("Current inventory:", sorted(inventory))
    print("< ================================================================================================== >\n")
    command = input("Enter command:\n")
    print("\n")

    Commands(command)

def Commands(command):
    global quit_game
    global current_room

    if command.lower() == "move":
        player_direction = input("Type a direction to move:\n")
        Move(player_direction)
    elif command.lower() == "use":
        Use()
    elif command.lower() == "inspect":
        Inspect()
    elif command.lower() == "options" or command.lower() == "help":
        HelpMessage()
    elif command.lower() == "map":
        DisplayMap()
    elif command.lower() == "exit":
        current_room = "Exit"
        quit_game = True
    else:
        print("\n< Invalid Input. Please refer to command list. Type 'help' or 'options' to view the list. >\n")


## Action Functions ##


# Function that moves the player
def Move(direction):
    global move_counter
    global quit_game # only True if player's current room is the bilge.
    global current_room

    move_counter += 1 # Player used MOVE.
    direction = direction.lower().capitalize() # Converting 'direction' variable to target format

    if direction in rooms[current_room]:
        # Direction exists. Move to that room.
        for loot, location in rooms[current_room].items():
            # Match player's 'loot' with room loot
            if direction == loot:
                # Move player to that room
                print("\nMoving", direction)
                current_room = location

                if current_room == "Unknown Portal":
                    quit_game = True
    else:
        # Direction does not exist in that room.
        print("Direction does not exist")

# Function that inspects room for items or hints
def Inspect():
    global move_counter
    global current_room
    global collectibles

    move_counter += 1
    print("You inspect your surroundings...\n")

    for location, pair in collectibles.items():
        for item, restriction in pair.items():
            if current_room == location and restriction == "N/A": # Target item reached
                print(room_desc[location])
                print("\nThere is no item to be obtained")
                break
            elif current_room == location and restriction == "FREE": # Target item reached, get item
                print(room_desc[location])
                print("\nObtained:", item)
                inventory.append(item)
                restriction = "N/A"
                pair[item] = restriction
                break
            elif current_room == location and restriction != "FREE" and restriction != "N/A":
                print(room_desc[location])
                print("\n" + str(item) + " is unobtainable at this moment.")
            else: # Target item not reached, continue iterating
                continue
            break
        continue

# Function that uses items to get other items
def Use():
    global move_counter
    global collectibles
    global current_room
    global room_desc
    global room_function
    global fixed_engine_room

    move_counter += 1

    # Unlock item in room
    for location, pair in collectibles.items():
        for item, restriction in pair.items():
            if current_room == location and item in inventory: # Item already exists in player's inventory.
                print("\nYou already have the item for this room.")
                break
            elif current_room == "Engine Room" and "Valve" in inventory and not fixed_engine_room: # Event 2
                print("< Turning on Power >")
                room_function[current_room] = 1
                fixed_engine_room = True
                for location, description in room_desc_update.items():
                    room_desc[location] = description # Updates every description for all rooms.
                room_desc[current_room] = room_desc_update[current_room][2]
                break
            elif current_room == location and restriction in inventory: # Paired item is found. Set locked item to FREE.
                print("\nYou used the " + str(restriction) + ". " + str(item) +
                      " is now obtainable. Type 'Inspect' to retrieve " + str(item))
                restriction = "FREE"
                pair[item] = restriction
                room_desc[location] = room_desc_update[location]  # Room changed, change description
                if current_room == "Engine Room" and not fixed_engine_room:
                    room_desc[location] = room_desc_update[location][1]
                    break
                room_function[location] = 1
                break
            elif current_room == location and restriction == "FREE": # Item in room is free to obtain
                print("\nAn item is located somewhere in this room. Type 'Inspect' to retrieve it.")
                break
            elif current_room == location and restriction == "N/A": # No item needs to be "Used" in the room
                print("\nThere is no item to be used here")
                break
            elif current_room == location and restriction not in inventory: # Need specific item to get tool.
                print("\nRequired item to get " + str(item) + " is not in your inventory")
                break
            else:
                continue

## Execution Game Functions ##


# Function that determines whether the player has won or lost
def Result():
    global item_counter # Must be 6 in order to win
    global room_counter # Must be 8 in order to win
    global fixed_engine_room # Must be true in order to win

    for value in room_function.values():
        room_counter += value
    print(room_counter)

    if current_room == "Unknown Portal" and item_counter == 6:
        if room_counter == 8 and fixed_engine_room == True:
            print("\n<<< CONGRATULATIONS >>>\n"
                  "\nYou won!\n"
                  "You completed all your tasks, gathered every item, fixed every room, turned on the power, and killed"
                  " the zombie!\n"
                  "You're a hero!\n")
        elif room_counter == 8 and not fixed_engine_room:
            print("\n>>> GAME OVER <<<\n"
                  "\nYou forgot to turn on the lights! The zombie delivered a fatal blow and knocked you out\n")
        else:
            print("\n>>> GAME OVER <<<\n"
                  "\nYour tasks were not fully completed.\n"
                  "Without the necessary equipment or power, the zombie overpowered you\n")
    else:
        print("\n>>> GAME OVER <<<\n"
              "You were unprepared and the zombie managed to escape\n")

    Stats()

# Print player stats by the end of the game.
def Stats():
    global item_counter
    global room_counter

    print("\n<< ============================================ >>\n")
    print("<< Player Stats >>")
    print("Total number of moves used:", move_counter) # Using MOVE, USE, or INSPECT adds 1 to the counter.
    print("Items collected: " + str(item_counter) + "/6")
    print("Rooms fixed: " + str(room_counter) + "/8")
    print("\n<< ============================================ >>\n")

# Function that runs most of the game's functions.
def Game():
    WelcomeMessage()
    while not quit_game:
        Menu()
    Result()


## Program Execution ##


if __name__ == '__main__':
    Game()

#TODO: Use changes description for engine room. Fix that