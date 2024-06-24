import random
import time
from logic import *

def display_info(knight):
    print()
    print("Current stats for " + knight["name"] + ": " "\n")
    for x, y in knight["stats"].items(): 
        print(str(x) + ": " + str(y))
    print()
    print("Current Combat Gear: \n")
    for x, y in knight["weaponry"].items(): 
        print(str(x) + ": " + str(y))
    print()
    print("Current inventory: \n")
    for x, y in knight["inventory"].items(): 
        print(str(x) + ": " + str(y))
    print()
    
def display_shop(items, knight):
    item_dict = {"sword": items[0], "shield": items[1], "armour": items[2], "horse": items[3]}
    flatten_list = []
    for category, list in item_dict.items():
        print(str(category) + " - items:")
        for item in list:
            flatten_list.append(item)
            print(str(item["id"]) + "- type: " + item["name"] + ", value: " + str(item["value"]) + ", price: " + str(item["price"]))

    try:
        print("Your current balance is: " + str(knight["inventory"]["gold"]))
        selection = int(input("Which item do you want to buy?"))
        item = flatten_list[selection]
        print("You have selected: " + str(item))
        if knight["gold"] < item["price"]:
            print("You do not have enough gold to purchase this item! Go Battle more!")
        else:
            weaponry = knight["weaponry"]
            weaponry[item["category"]] = item["name"]
            print("You have bought: " + str(item["category"]) + " " + str(item["name"]))
    
    except:
        print("You need to select a valid item.") 
        display_shop(items, knight)
        
    # Psudeo code
    # 1. Flatten items so can select by id ✅
    # 2. make sure item id exist in list with try except KeyError ✅
    # 3. if item exists and we have enough money override property and subtract balance
    # 4 if item exist and we dont hae enough money re run display shop
    # 5. allow input of knight so we can assign item to knight
    
def create_knight(knights):  
    #Create a new dictionary to hold knights data
    knights_data = {}
    
    print("Lets create a knight!")
    
    # Set the information up for the knight
    knights_data["name"] = ("Sir " + str(input("What is the knights name: ")))
    knights_data["stats"] = {"level": int(1), 
                             "xp": int(10), 
                             "max_health": int(100),
                             "current_health": int(70), 
                             "attack": int(10), 
                             "defence": int(10)}
    knights_data["weaponry"] = {"horse": "default", "sword": "default", "shield": "default", "armour": "default"}
    knights_data["inventory"] = {"bandages" : int(5), "throwing_knife": int(5), "gold": int(100)}
    
    # Adds all the knight info to knights array
    knights.append(knights_data)

    print("Creating your knight...")
    # time.sleep(1)
    print("Training your Knight...")
    # time.sleep(3)
    print("Knight is made!")
    print("Here's their stats:")
    display_info(knights_data)
    menu(knights_number)

# Call a knight and change their properties
def change_data(knights):
    print("--- What would you like to update? ---")
    print("0: Back To Knight Selection")
    print("1: Knight's name: " + knights["name"])
    # ADD MORE STUFF TO CHANGE HERE.
    # Catches any inputs that aren't a number.
    selection = int(input("Select your option: "))

    if selection == 1:
        knights["name"] = str(input("What is their new name? "))
        print("Your knight's new name is: " + knights["name"])
    elif selection == 0:
        select_knight(knights)
    else:
        print("--- Please select a valid option ---")
            

# Show current knights and select one

def select_knight(knights):
    
    # Reset the list to print all the knights
    knights_number = 0
    print("What knight do you want to update? \n")
    try:
        print("0- Back To Menu")
        while knights_number < int(len(knights)):
            print(str(knights_number + 1) + "- Knight's name: " + str(knights[knights_number]["name"]))
            knights_number += 1
        select = (int(input("\nSelect the Knights number: ")) -1)
        if select >= 0:
            return (knights[select])
    except:
        print("Please select a valid option")
        select_knight(knights)
    
# Menu options to choose selection
def menu(knights_number):
    # Display options printed to console
    print("What do you want to do?")
    print()
    print("1: Create a new knight")
    print("2: Update your knight")
    print("3: Display a current knight stats")
    print("4: Visit shop")
    print("0: Exit")
    
    # Allows a selection and verify input is keyboard number
    
    try: 
        #  Take user input
        select = int(input("Select Option: "))
        print()
        
        # Creates a new knight
        if select == 1:
            create_knight(knights)
            
            # Print out the knight that was made
            print("\n--- Your Knight --- \n")
            print("Knight's name: " + str(knights[knights_number][0] + "\n"))
            knights_number += 1
            menu(knights_number)
        
        elif select == 2:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
                menu(knights_number)
            else:
                knight = select_knight(knights)
                change_data(knight)
                menu(knights_number)
                
        elif select == 3:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
                menu(knights_number)
            else:
                display_info(select_knight(knights))
                menu(knights_number)
        
        elif select == 4:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
                menu(knights_number)
            else:
                display_shop(items, select_knight(knights))
                menu(knights_number)
                
            
        elif select == 0:
            print("--- All your knights!---\n")
            
            #  Reset the knights_number, so we can count and iterate all the knights
            knights_number = 0
            
            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + "- Knight's name: " + str(knights[knights_number][0]))
                knights_number += 1
            
            if int(len(knights)) == 0:
                print("Wait... You have no knights! Have a number: " + str(random.randint(0, 100)))
            
        # For DEV - Check what happens if you remove this. Why do we need to catch int twice?
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
print("Welcome to our Kingdom!")
print("You need to create Knights to defend the Kingdom with.")
# menu(knights_number)
create_knight(knights)
print(combat.heal(knights[0]))
