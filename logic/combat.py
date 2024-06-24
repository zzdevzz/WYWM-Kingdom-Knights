# Make it so it's chance based like runescape.
# Make it so there's timeouts between each hit.

from data import items

def get_item(id,items):
    

def battle(person1, person2):
    pass

def heal(knight):
    heal_amount = int(15)
    current_health = knight["stats"]["current_health"]
    max_health = knight["stats"]["max_health"]
    if current_health == max_health:
        print("Already at max health!")
    elif knight["inventory"]["bandages"] == 0:
        print("You have no bandages left!")
    else:
        current_bandages = knight["inventory"]["bandages"]
        current_bandages -= 1
        current_health += heal_amount
        current_health = current_health if current_health < max_health else max_health
        print("Knight healed")
        print("Health: " + str(current_health) + " - You have " + str(current_bandages) + " bandages left.")

def is_dead(knight):
    if knight["stats"]["current_health"] <= 0:
        print("Oh no! " + str(knight["name"]) + " is dead!!!")
        return
    else:
        return

def generate_opponent(knight, items):
    oppenent = {}
    
def battle_stats(knight):
    sword = knight["weaponry"]["sword"]
    horse = knight["weaponry"]["horse"]
    armour = knight["weaponry"]["armour"]
    shield = knight["weaponry"]["shield"]
    
    defence_total = int(knight["stats"]["defence"] + knight["weaponry"]["horse"]["value"])
    attack_total = int(knight["stats"]["attack"] + knight["weaponry"]["sword"]["value"])
    return {"attack": attack_total, "defence": defence_total}