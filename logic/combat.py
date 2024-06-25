import random
import time
from random import randrange
# def find_item_by_id(id,items):
#     inventory = flatten_list = []
#     for category in items:
#         for item in category:
#             flatten_list.append(item)
#     for item in inventory:
#         if item["item"] == id:
#             return item
#     return None  # Return None if no item with the given ID is found
    
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

def is_dead(knight, knight_health, opp_health):
    if knight_health <= 0:
        print("Oh no! " + str(knight["name"]) + " is dead!!!")
    elif opp_health <= 0:
        print("Congratulations! You have won! The Kingdom thanks you!")
        print("You have been granted 10 xp!")
        knight["stats"]["xp"] += int(10) 
    else:
        return

def battle_stats(knight):
    sword = knight["weaponry"]["sword"]["value"]
    horse = knight["weaponry"]["horse"]["value"]
    armour = knight["weaponry"]["armour"]["value"]
    shield = knight["weaponry"]["shield"]["value"]
    
    defence_total = int(knight["stats"]["defence"]) + armour + shield
    attack_total = int(knight["stats"]["attack"]) + sword
    health_total = int(knight["stats"]["health"]) + horse
    return {"attack": attack_total, "defence": defence_total, "health": health_total}

def generate_opponent(stats):
    names = ["Tristan", "Tywin", "Goraf", "Luther"]
    opponent = {**stats}
    opponent["name"] = random.choice(names)
    return opponent
        
def damage_dealt(stats_1, stats_2):
    attack_1 = stats_1["attack"]
    max_hit_1 = round(attack_1 / 1)
    
    defence_2 = stats_2["defence"]
    
    successful_attack = random.randint(round(attack_1/4),attack_1) > random.randint(round(defence_2/4), defence_2)
    damage = round(random.random(0.3, 1.0) * max_hit_1)
    if successful_attack:
        return damage
    else:
        return 0
        
    
def battle(knight):
    print("Commencing Battle!")
    print()
    knight_stats = battle_stats(knight)
    # print("Knight stats " + str(knight_stats))
    opp_stats = generate_opponent(knight_stats)
    # print("Opponent stats " + str(opp_stats))
    knight_health = knight_stats["health"]
    opp_health = opp_stats["health"]
    
    while knight_health > 0 and opp_health > 0:
        
        # Knight attacks opponent
        damage = damage_dealt(knight_stats, opp_stats)
        opp_health -= damage
        opp_health =  opp_health if opp_health >= 0 else 0

        print("Knight " + knight["name"] + " caused " + str(damage) + " damage to " + opp_stats["name"] + ".")
        print("Knight " + opp_stats["name"] + " has " + str(opp_health) + " health remaining.") 
        print()
        is_dead(knight, knight_health, opp_health)

        time.sleep(0.5)
        
        # Opponent attacks knight
        damage = damage_dealt(knight_stats, opp_stats)
        knight_health -= damage
        knight_health =  knight_health if knight_health >= 0 else 0

        print("Sir " + opp_stats["name"] + " caused " + str(damage) + " damage to " + knight["name"] + ".")
        print(knight["name"] + " has " + str(knight_health) + " health remaining.") 
        print()
        is_dead(knight, knight_health, opp_health)
        time.sleep(0.5)
        
        