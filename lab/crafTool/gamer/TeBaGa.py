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

# Todo -- Show the goal of the game and move commands -- Make this the HelpMessage
def Show_instructions():
    # Print out the main menu and the commands
    print("\n<<-=============================================================================================->>\n")
    print('                     Welcome to Portal Protector Text Adventure Game.')
    print('         Collect 6 items to with the game, or be devoured by the hungry Wendigo.')
    print('     Move commands: (n)go North, (e)go East, (s)go South, (w)go West, (exit) to exit')
    print('                          Add to Inventory: get "item name"')





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

gear = { # Fixme collectibles FREE change
    'WashRoom': { 'Elemental Wand': 'FREE'},
    'Foyer': {'Shoes of Hermes': 'FREE'},
    'Temple': {'Samurai Armor': 'FREE'},
    'Crystal Ball Surveillance Room': {'Crystal ball': 'FREE'},
    'Kitchen': {'Salt Cured Meat': 'FREE'},
    'Wine Cellar': {'Potion': 'FREE'}
    # 'Unknown Portal': {'item': 'Wendigo'}   # bad guy
}

room_desc = {
    'WashRoom': 'This is a nice bathroom but why are there so many mirrors',
    'Foyer': 'You see a sign that ask you to remove your shoes',
    'Temple': 'Just a open and empty room with a burn pit in the middle looks like it was used recently',
    'Crystal Ball Surveillance Room': 'Why do they work like ring cameras lol ',
    'Kitchen': 'Smells a lil musky must be the broccoli',
    'Wine Cellar': 'Grab some wine or look for the ',
    'Unknown Portal': 'This is when you realize that stench wasn\'t the broccoli'   # bad guy
}

room_desc_updater = {
    'WashRoom': 'This is a nice bathroom but really creapy',
    'Foyer': 'Still can\'t find that damn cat',
    'Temple': 'kitty kitty ',
    'Crystal Ball Surveillance Room': 'Why do they work like ring cameras lol ',
    'Kitchen': 'Smells a lil musky must be the broccoli',
    'Wine Cellar': 'Grab some wine or look for the ',
    'Unknown Portal': 'this isn\'t going to be fun'   # bad guy
}



# If the player is lost and needs to know where they are located
# Todo - make a display map that shows the players location on the map
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
def WelcomeMessage():
    print('Welcome to my game')


def DisplayMap():
    print('Show user commands')




# Todo -- Startint point
def Main_menu():
    global current_room
    global item_counter
    global quit_game

    item_counter = len(inventory)
    print("\n<<-=============================================================================================->>\n")
    print('Your currently in: {}'.format(current_room))
    print('The Items you collect: {}'.format(inventory))
    print("\n<<-=============================================================================================->>\n")
    user_command = input('Enter your command:\n')  # command
    Commands(user_command)



# Todo  ---- >  Menu()
def Commands(user_command):
    global quit_game
    global current_room

    if user_command.lower() == "move":
        player_direction = input("Type a direction to move:\n")
        MoveMent(player_direction)
    elif user_command.lower() == "story":
        show_story()
#     elif user_command.lower() == "use":
#         Use()
#     elif user_command.lower() == "inspect":
#         Inspect()
    elif user_command.lower() == "options" or user_command.lower() == "help":
        Show_instructions()
    elif user_command.lower() == "map":
        DisplayMap()
    elif user_command.lower() == "exit":
        current_room = "Exit"
        quit_game = True
    else:
        print("\n< Invalid Input. Please refer to command list. Type 'help' or 'options' to view the list. >\n")


 # TODO ---  Move()
def MoveMent(direction):
    global move_counter
    global quit_game    # only True if player's current room is the uknown portal
    global current_room

    move_counter += 1 # Player used MOVE.
    direction = direction.lower().capitalize() # Converting 'direction' variable to target format

    if direction in rooms[current_room]:
        # Move player to that room
        for loot, location in rooms[current_room].items():
            if direction == loot:
                print('\nMoving to the {}'.format(direction))
                current_room = location

                if current_room == 'Unknown Portal':
                    quit_game = True

    else:
        # Direction does not exist in that room.
        print("Direction does not exist")






# Todo - how to use items
def use():
    pass


# Todo - Let player inspect the room to look for item
def inspect():
    pass

# Todo - Set the fight sequence
def fight():
    pass

# Todo - print out all of the commands
def Result():

    pass


# Todo - This is where the current game status is held
    # player items, players location
def Status():
    global item_counter
    global room_counter

    print("\n<< ============================================ >>\n")
    print("<< Player Stats >>")
    print("Total number of moves used:", move_counter)  # Using MOVE, USE, or INSPECT adds 1 to the counter.
    print("Items collected: " + str(item_counter) + "/6")
    # print("Rooms fixed: " + str(room_counter) + "/8")
    print("\n<< ============================================ >>\n")



# Fixme that Function that runs most of the game's functions.
def Game():
    # WelcomeMessage()
   # show_story()
   # show_instructions()
    while not quit_game:
        Main_menu()



## Program Execution ##
#
#
if __name__ == '__main__':
    Game()


