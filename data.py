items_sword = [{"name": "default", "value": int(10), "price": int(10), "id": int(1), "category": "sword"},
                {"name": "bronze", "value": int(20), "price": int(20), "id": int(2), "category": "sword"},
                {"name": "steel", "value": int(30), "price": int(80), "id": int(3), "category": "sword"},
                {"name": "obsedian", "value": int(50), "price": int(100), "id": int(4), "category": "sword"}]

items_shield = []
items_armour = []
length = len(items_sword)

for item in items_sword:
    shield_item = {**item}
    armour_item = {**item}
    shield_item["id"] = int(item["id"] + length)
    shield_item["category"] = "shield"
    items_shield.append(shield_item)
    armour_item["id"] = int(item["id"] + (length * 2))
    armour_item["category"] = "armour"
    items_armour.append(armour_item)
    
items_horse = [{"name": "default", "value": int(50), "price": int(10), "id": int(13), "category": "horse"},
                {"name": "medium", "value": int(20), "price": int(50), "id": int(14), "category": "horse"},
                {"name": "large", "value": int(40), "price": int(100), "id": int(15), "category": "horse"},
                {"name": "supreme", "value": int(60), "price": int(200), "id": int(16), "category": "horse"}]

items = [items_sword, items_shield, items_armour, items_horse]

item2 = items_sword + items_shield
print(item2)