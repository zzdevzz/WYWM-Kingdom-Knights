import random
import time
from logic import *
# Call to create a new knight

items_attack = {"default": int(10), "bronze": int(20), "steel": int(30), "obsedian": int(50)}
items_defence = {"default": int(10), "bronze": int(20), "steel": int(30), "obsedian": int(50)}
items_horse = {"default": int(50), "medium": int(65), "large": int(80), "supreme": int(100)}

def display_info(knight):
    print("Current stats for " + knight["name"] + ": " "\n")
    print()
    for x, y in knight["stats"].items(): 
        print(str(x) + ": " + str(y))
    print()
    print("Current Weaponry: \n")
    for x, y in knight["weaponry"].items(): 
        print(str(x) + ": x " + str(y))
    print("Current inventory: \n")
    for x, y in knight["inventory"].items(): 
        print(str(x) + ": x " + str(y))
    print()
    
def calculate_player_stats(knight):
    pass
    
def create_knight(knights):  
    #Create a new dictionary to hold knights data
    knights_data = {}
    
    print("Lets create a knight!")
    
    # Set the information up for the knight
    knights_data["name"] = ("Sir " + str(input("What is the knights name: ")))
    knights_data["stats"] = {"level": int(1), 
                             "xp": int(10), 
                             "max_health": int(100),
                             "current_health": int(100), 
                             "attack": int(10), 
                             "strength": int(10)}
    knights_data["weaponry"] = {"horse": "default", "sword": "default", "shield": "default", "armour": "default"}
    knights_data["inventory"] = {"bandages" : int(5), "throwing_knife": int(5), "gold": int(100)}
    
    # Adds all the knight info to knights array
    knights.append(knights_data)

    print("Creating your knight...")
    time.sleep(1)
    print("Training your Knight...")
    time.sleep(3)
    print("Knight is made!")
    print("Here's their stats:")
    display_info(knights_data)

# Call a knight and change their properties
def change_data(knights):
    print("--- What would you like to update? ---")
    print("1: Knight's name: " + knights[0])
    # ADD MORE STUFF TO CHANGE HERE.
    # Catches any inputs that aren't a number.
    try:

        selection = int(input("Select your option: "))

        if selection == 1:
            if knights_number == 0:
                print("You have a knight!")
            knights[0] = str(input("What is their new name? "))
            print("Your knight's new name is: " + knights[0])
            return 
        else:
            print("--- Please select a valid option ---")
            
    except:
        print("--- Try Again! ---")
        change_data(knights)

# Show current knights and select one

def select_knight(knights):
    
    # Reset the list to print all the knights
    knights_number = 0
    print("What knight do you want to update? \n")
    while knights_number < int(len(knights)):
        print(str(knights_number + 1) + "- Knight's name: " + str(knights[knights_number][0]))
        knights_number += 1
    select = (int(input("\nSelect the Knights number: ")) -1)
    change_data(knights[select])
    
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
                select_knight(knights)
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
    except:
        print("--- Try Again! ---\n")
        menu(knights_number)

# Setting the scene

knights_number = 0
knights = []

# Run the program
print("Welcome to our Kingdom!")
print("You need to create Knights to defend the Kingdom with.")
# menu(knights_number)
create_knight(knights)
print(knights)
print(combat.heal(knights[0]))
