# Make it so it's chance based like runescape.
# Make it so there's timeouts between each hit.

def battle(person1, person2):
    pass

def heal(knight):
    heal_amount = int(15)
    if knight["current_health"] == knight["max_health"]:
        print("Already at max health!")
    elif knight["inventory"]["bandages"] == 0:
        print("You have no bandages left!")
    else:
        current_health = knight["current_health"]
        current_bandages = knight["inventory"]["bandages"]
        current_bandages -= 1
        current_health += heal_amount
        current_health if current_health < knight["max_health"] else knight["max_health"]
        print("Knight healed")
        print("Health: " + str(current_health) + " - You have " + str(current_bandages) + " bandages left.")
