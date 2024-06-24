items_attack = [{"name": "default", "value": int(10), "price": int(10), "id": int(1)},
                {"name": "bronze", "value": int(20), "price": int(20), "id": int(2)},
                {"name": "steel", "value": int(30), "price": int(80), "id": int(3)},
                {"name": "obsedian", "value": int(50), "price": int(100), "id": int(4)}]

items_defence = []
length = len(items_attack)

for item in items_attack:
    new_item = {**item}
    new_item["id"] = int(new_item["id"] + length)
    items_defence.append(new_item)
    
items_horse = [{"name": "default", "value": int(50), "price": int(10), "id": int(9)},
                {"name": "medium", "value": int(20), "price": int(50), "id": int(10)},
                {"name": "large", "value": int(40), "price": int(100), "id": int(11)},
                {"name": "supreme", "value": int(60), "price": int(200), "id": int(12)}]

items = [items_attack, items_defence, items_horse]
