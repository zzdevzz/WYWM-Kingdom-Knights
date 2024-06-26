import random
import time
from logic import *

def display_info(knight):
    """ Displays current information about night including current name, combat stats, gear and inventory"""
    
    print()
    print("Current base stats for " + knight["name"] + ": " "\n")
    print(r"""       
          __      _
         /__\__  //
        //_____\///
       _| /-_-\)|/_
      (___\ _ //___\
      (  |\\_/// * \\
       \_| \_((*   *))
       ( |__|_\\  *//
       (o/  _  \_*_/
       //\__|__/\
      // |  | |  |
     //  _\ | |___)
    //  (___|
          """)
    print("====================")
    for x, y in knight["stats"].items(): 
        print(str(x) + ": " + str(y))
    print()
    print("Current Combat Gear: \n")
    for x, y in knight["weaponry"].items(): 
        print(str(x) + ": " + str(y["name"]))
    print()
    print("Current inventory: \n")
    for x, y in knight["inventory"].items(): 
        print(str(x) + ": " + str(y))
    print("====================")
    print()
    
def display_shop(items, knight):
    """ Displays all items available in shop from data file."""
    
    flatten_list = []
    print()
    for category in items:
        print(str(category[0]["category"]) + "s :")
        for item in category:
            flatten_list.append(item)
            print(str(item["id"]) + " - type: " + item["name"] + ", value: " + str(item["value"]) + ", price: " + str(item["price"]))
        print()
    try:
        print("Your current balance is: " + str(knight["inventory"]["gold"]))
        selection = int(input("Which item do you want to buy? ")) - 1
        print()
        item = flatten_list[selection]
        print("You have selected: " + str(item["name"]) + " " + str(item["category"]))
        if knight["inventory"]["gold"] < item["price"]:
            print("You do not have enough gold to purchase this item! Go battle more!")
        else:
            weaponry = knight["weaponry"]
            weaponry[item["category"]] = item
            knight["inventory"]["gold"] -= item["price"]
            print("You have bought: " + str(item["name"]) + " " + str(item["category"] + " for " + str(item["price"]) + " gold."))
            print("You have now have " + str(knight["inventory"]["gold"]) + " gold left.")
            print("Your knight inspects his new item and equips it!")
            print()
    
    except Exception as e:
        print("You need to select a valid item.")
        print(f"An error occurred: {e}")
        print(f"Type of error: {type(e).__name__}")
        display_shop(items, knight)
            
def create_knight(knights):  
    """Create a new knight and add to list of knights."""
    
    knight_data = {}
    
    print("Lets create a knight!")
    
    name = ""
    while name == "":
        name = str(input("What is the knights name? Sir: "))
    # Set the information up for the knight
    knight_data["name"] = ("Sir " + name)
    print()
    knight_data["stats"] = {"level": int(1), 
                             "xp": int(10), 
                             "health": int(100),
                             "attack": int(10), 
                             "defence": int(10)}
    knight_data["weaponry"] = {"horse": items_horse[0], "sword": items_sword[0], "shield": items_shield[0], "armour": items_armour[0]}
    knight_data["inventory"] = {"gold": int(100)}
    
    # Adds all the knight info to knights array
    knights.append(knight_data)
    
    # Displays Knight being made with their stats.

    print("Creating your knight...")
    time.sleep(1)
    print("Training your Knight...")
    time.sleep(2)
    print("Knight is made!")
    display_info(knight_data)



def change_data(knight):
    """Call a knight and change their properties."""
    
    print()
    print("--- What would you like to update? ---")
    print("0: Back To Knight Selection")
    print("1: Knight's name: " + knight["name"])
    print()

    # Catches any inputs that aren't a number.
    selection = int(input("Select your option: "))

    if selection == 1:
        knight["name"] = str("sir " + input("What is their new name? Sir: "))
        print("Your knight's new name is sir: " + knight["name"])
    elif selection == 0:
        select_knight(knights)
    else:
        print("--- Please select a valid option ---")
                

def select_knight(knights):
    """Displays all knights and allows user to select one."""
    
    # Reset the list to print all the knights
    knights_number = 0
    print("What knight do you want to choose? \n")
    try:
        print("0- Back To Menu")
        while knights_number < int(len(knights)):
            print(str(knights_number + 1) + "- Knight's name: " + str(knights[knights_number]["name"]))
            knights_number += 1
        select = (int(input("\nSelect the Knights number: ")) -1)
        if select >= 0:
            return (knights[select])
        else:
            menu(knights_number)
            print("this was run after menu")
            return
    except:
        print("Please select a valid option")
        select_knight(knights)
    

def menu(knights_number):
    """Default app menu display all options available."""
    
    # Display options printed to console
    print()
    print("What do you want to do?")
    print()
    print("1: Create a new knight")
    print("2: Update your knight")
    print("3: Display knight stats")
    print("4: View all knights")
    print("5: Visit shop to upgrade Knight")
    print("6: Battle opponents")
    print("0: Exit")
    
    # Allows a selection and verify input is keyboard number
    
    try: 
        #  Take user input
        print()
        select = int(input("Select Option: "))
        print()
        
        # Creates a new knight
        if select == 1:
            create_knight(knights)
            
            # Print out the knight that was made
            print("\n--- Your Knight --- \n")
            print("Knight's name: " + str(knights[knights_number]["name"] + "\n"))
            knights_number += 1
            menu(knights_number)
        
        # Change selected knight data
        elif select == 2:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
                menu(knights_number)
            else:
                knight = select_knight(knights)
                change_data(knight)
                menu(knights_number)
                
        # Display information for selected knight        
        elif select == 3:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
                menu(knights_number)
            else:
                display_info(select_knight(knights))
                menu(knights_number)
        
        # Displays all knights currently created
        elif select == 4:
            print("--- All your knights!---\n")
            
            #  Reset the knights_number, so we can count and iterate all the knights
            knights_number = 0
            
            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + "- Knight's name: " + str(knights[knights_number]["name"]))
                knights_number += 1
            
            if int(len(knights)) == 0:
                print("Wait... You have no knights! Have a number: " + str(random.randint(0, 100)))
                
            print("-------------------------")
            menu(knights_number)
        
        # Allows users to see and buy all items available in shop from data file
        elif select == 5:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
                menu(knights_number)
            else:
                display_shop(items, select_knight(knights))
                menu(knights_number)
        
        # Select a chosen knight and start a battle
        elif select == 6:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
                menu(knights_number)
            else:
                knight = select_knight(knights)
                battle(knight)
                menu(knights_number)
        
        # Exit the program
        elif select == 0:
            print("Goodbye")
            print()
        else:
            print("--- Try Again! ---\n")
            menu(knights_number)
    
    #  If input isn't an integer
    except Exception as e:
        print("--- Try Again! ---\n")
        print(f"An error occurred: {e}")
        print(f"Type of error: {type(e).__name__}")
        menu(knights_number)

# Setting the scene

knights_number = 0
knights = []

# Run the program
print(r"""
Welcome to our Kingdom!



                   T~~
               |
              /"\
      T~~     |'| T~~
  T~~ |    T~ WWWW|
  |  /"\   |  |  |/\T~~
 /"\ WWW  /"\ |' |WW|
WWWWW/\| /   \|'/\|/"\
|   /__\/]WWW[\/__\WWWW
|"  WWWW'|I_I|'WWWW'  |
|   |' |/  -  \|' |'  |
|'  |  |LI=H=LI|' |   |
|   |' | |[_]| |  |'  |
|   |  |_|###|_|  |   |
'---'--'-/___\-'--'---' 
      """)
time.sleep(3)
print("We need you to create Knights to defend the Kingdom with.")
create_knight(knights)
menu(knights_number)