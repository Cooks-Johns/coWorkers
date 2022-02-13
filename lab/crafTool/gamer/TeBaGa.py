"""
 Name:

 In the Foyer there are the shoesOfHermes,
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

"""

# Todo -- Show the goal of the game and move commands
def show_instructions():
    # Print out the main menu and the commands
    print("\n<<-=============================================================================================->>\n")
    print('                     Welcome to Portal Protector Text Adventure Game.')
    print('         Collect 6 items to with the game, or be devoured by the hungry Wendigo.')
    print('     Move commands: (n)go North, (e)go East, (s)go South, (w)go West, (exit) to exit')
    print('                          Add to Inventory: get "item name"')
    print("\n<<-=============================================================================================->>\n")





def show_story():
    print("\n<<-=============================================================================================->>\n")
    print('                 Portal Protector           \n'
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
    print("\n<<-=============================================================================================->>\n")




# Fixme ------ A dictionary linking a room to other rooms
#  and linking one item for each room except the Start room (Great Hall) and the room containing the villain
rooms = {
    'WashRoom': {'West': 'Foyer', 'item': 'Elemental Wand'},
    'Foyer': {'North': 'Temple', 'East': 'Washroom', 'item': 'Shoes of Hermes'},
    'Temple': {'South': 'Foyer', 'North': 'Kitchen', 'West': 'Crystal Ball Surveillance Room', 'item': 'Samurai Armor'},
    'Crystal Ball Surveillance Room': {'East': 'Foyer', 'item': 'Crystal ball'},
    'Kitchen': {'South': 'Temple', 'East': 'Food Storage', 'item': 'Salt Cured Meat'},
    'Wine Cellar': {'South': 'Unknown Portal', 'item': 'Potion'},
    'Unknown Portal': {'North': 'Wine Celler', 'item': 'Wendigo'}   # bad guy
}





# Todo -- Player must inspect room for item in order to leave room
room_items = {
    'WashRoom': 1,
    'Foyer': 1,
    'Temple': 1,
    'Crystal Ball Serveillance Room': 1,
    'Kitchen': 1,
    'Wine Cellar': 1,
    'Unknown Portal': 1
}

gear = {
    'WashRoom': {}
}



# If the player is lost and needs to know where they are located they can t
def DisplayMap():
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
          "               |________| <-- |__________|       |____________________|       \n")




# Todo - Global Vars

current_room = "Foyer"
move_counter = 0  # Total moves in the game.
item_counter = 0  # How many total items have been retrieved
room_counter = 0  # How many rooms are fully functional
fixed_engine_room = False
quit_game = False
inventory = []


# Fixme

def MoveMent(direction):
    global move_counter
    global quit_game # only True if player's current room is the bilge.
    global current_room

    move_counter += 1 # Player used MOVE.
    direction = direction.lower().capitalize() # Converting 'direction' variable to target format

    if direction in rooms[current_room]:
        # Move player to that room
        print("\nMoving", direction)
        current_room = rooms.get(direction)

    else:
        # Direction does not exist in that room.
        print("Direction does not exist")
    return current_room






# Todo -- Startint point
def Main_menu():
    print("\n<<-=============================================================================================->>\n")
    print('Your currently in: {}'.format(current_room))
    print('The Items you collect: {}'.format(inventory))
    print("\n<<-=============================================================================================->>\n")
    user_command = input('Enter your command:\n')
    Commands(user_command)



# Todo
def Commands(command):
    global quit_game
    global current_room

    if command.lower() == "move":
        player_direction = input("Type a direction to move:\n")
        MoveMent(player_direction)
    elif command.lower() == "story":
        show_story()
#     elif command.lower() == "use":
#         Use()
#     elif command.lower() == "inspect":
#         Inspect()
#     elif command.lower() == "options" or command.lower() == "help":
#         HelpMessage()
    elif command.lower() == "map":
        DisplayMap()
    elif command.lower() == "exit":
        current_room = "Exit"
        quit_game = True
    else:
        print("\n< Invalid Input. Please refer to command list. Type 'help' or 'options' to view the list. >\n")



# Todo
# Todo
# Todo
# Todo
# Todo
# Todo
def Status():
    global item_counter
    global room_counter
    global room_engin








# Fixme that Function that runs most of the game's functions.
def Game():
    # WelcomeMessage()
   # show_story()
   # show_instructions()
    while not quit_game:
        Main_menu()
    Status()


## Program Execution ##
#
#
if __name__ == '__main__':
    Game()


