import math

def calculate_level(xp):
    return int(math.floor(xp/10))

def set_stats(knight):
    # Destructure values in dictionary of player stats
    level, xp, max_health, current_health, attack, defence = knight.values()
    base_value = int(10)
    attack = defence = int(base_value * level)
    max_health = int(100) + base_value * level