import random
import time
from .level import *

def rest():
    
    """Generates rest text to console"""
    print("You need to rest to recover your health...")
    time.sleep(2)
    print("resting...")
    time.sleep(2)
    print("resting more...")
    time.sleep(2)
    print("All rested! Your health has now fully recovered.")
    print()
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
    print()
    

def is_dead(knight, knight_health, opp_health):
    
    """Checks if either knight is dead.
    
    Assigns correct xp and gold amount if player has one,
    handles error to shows who won.
    """
    
    if knight_health <= 0:
        knight["stats"]["xp"] -= int(10) if knight["stats"]["xp"] > 10 else int(10)
        knight["stats"]["level"] = calculate_level(knight["stats"]["xp"]) 
        raise Exception("KnightLost")
    elif opp_health <= 0:
        knight["stats"]["xp"] += int(10)
        knight["inventory"]["gold"] += int(50)
        knight["stats"]["level"] = calculate_level(knight["stats"]["xp"]) 
        raise Exception("KnightWon")
    else:
        return


def battle_stats(knight):
    
    """Calculates battle stats for knight based on player stats and gear stats."""
    sword = knight["weaponry"]["sword"]["value"]
    horse = knight["weaponry"]["horse"]["value"]
    armour = knight["weaponry"]["armour"]["value"]
    shield = knight["weaponry"]["shield"]["value"]
    
    defence_total = int(knight["stats"]["defence"]) + armour + shield
    attack_total = int(knight["stats"]["attack"]) + sword
    health_total = int(knight["stats"]["health"]) + horse
    return {"attack": attack_total, "defence": defence_total, "health": health_total}


def generate_opponent(stats):
    
    """Generates an opponent identical to player stats with different name."""
    names = ["Tristan", "Tywin", "Goraf", "Luther"]
    opponent = {**stats}
    opponent["name"] = random.choice(names)
    return opponent

      
def damage_dealt(stats_1, stats_2):
    
    """Determines if attack is successful and damage amount based on both knights stats."""
    attack_1 = stats_1["attack"]
    max_hit_1 = attack_1
    
    defence_2 = stats_2["defence"]
    
    successful_attack = random.randint(round(attack_1/4),attack_1) > random.randint(round(defence_2/4), defence_2)
    damage = round(random.uniform(0.3, 1.0) * max_hit_1)
    if successful_attack:
        return damage
    else:
        return 5
        
    
def battle(knight):
    
    """Produces a battle based on given knight.
    
    Will use damage_dealt, battle_stats, generate_opponent and is_dead functions to help,
    fully rng based so battles lengths can vary."""
    
    print("Commencing Battle!")
    print(r"""
         *_   _   _   _   _   _ *
 ^       | `_' `-' `_' `-' `_' `|       ^
 |       |                      |       |
 |  (*)  |_   _   _   _   _   _ |  \^/  |
 | _<">_ | `_' `-' `_' `-' `_' `| _(#)_ |
o+o \ / \0                      0/ \ / (=)
 0'\ ^ /\/                      \/\ ^ /`0
   /_^_\ |                      | /_^_\
   || || |                      | || ||
   d|_|b_T______________________T_d|_|b
          """)
    time.sleep(2)
    print()
    knight_stats = battle_stats(knight)
    opp_stats = generate_opponent(knight_stats)
    knight_health = knight_stats["health"]
    opp_health = opp_stats["health"]
    
    # Allows us to break out loop while loop if fight stops before code reaches end.
    try:
        while knight_health > 0 and opp_health > 0:
            
            # Knight attacks opponent
            damage = damage_dealt(knight_stats, opp_stats)
            opp_health -= damage
            opp_health =  opp_health if opp_health >= 0 else 0

            print("=||======>")
            print("Knight " + knight["name"] + " caused " + str(damage) + " damage to " + opp_stats["name"] + ".")
            print("Knight " + opp_stats["name"] + " has " + str(opp_health) + " health remaining.") 
            print()
            is_dead(knight, knight_health, opp_health)

            time.sleep(0.5)
            
            # Opponent attacks knight
            damage = damage_dealt(knight_stats, opp_stats)
            knight_health -= damage
            knight_health =  knight_health if knight_health >= 0 else 0

            print("<======||=")
            print("Sir " + opp_stats["name"] + " caused " + str(damage) + " damage to " + knight["name"] + ".")
            print(knight["name"] + " has " + str(knight_health) + " health remaining.") 
            print()
            is_dead(knight, knight_health, opp_health)
            time.sleep(0.5)
            
    # Prints result depending on outcome.        
    except Exception as e:
        if str(e) == "KnightLost":
            print("Oh no! " + str(knight["name"]) + " lost!")
            print()
            rest()
        elif str(e) == "KnightWon":
            print("Congratulations! You have won! The Kingdom thanks you!")
            print("You have been granted 10 xp and won 50 gold!")
            print()
            rest()
            