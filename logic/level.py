import math

def calculate_level(xp):
    
    """Set level based on current xp"""
    return int(math.floor(xp/10))

def set_stats(knight):
    
    """Set and update knight's stats based on the level."""
    
    base_value = int(10)
    level = knight["stats"]["level"]
    
    # Calculate new stats
    attack = defence = base_value * level
    max_health = 100 + base_value * level

    # Update the knight's stats in the dictionary
    knight["stats"]["attack"] = attack
    knight["stats"]["defence"] = defence
    knight["stats"]["max_health"] = max_health