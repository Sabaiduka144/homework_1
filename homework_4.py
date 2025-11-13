pet = {
    'name': 'Lua',
    'age': 3,
    'species': 'cat'
}
print(f"\nMy {pet['species']}s name is {pet['name']} and it is {pet['age']} years old")

print("\nWelcome to your adventure")

user_name = input("Enter your name: ").strip().title()

hero = {
    'name': user_name,
    'class': 'Warrior',
    'race': 'Human',
    'level': 1,
    'gold': 100,
    'hp': 120,
    'xp': 0,
    "inventory": []    
}

print("\nYour hero sheet:")
for key, value in hero.items():
    print(f" {key}: {value}")
    
print("\nYou find a wooden chest...")

chest = [
    {"name": "sword", "damage": 10, "rarity": "common", "weight": 5},
    {"name": "bow", "damage": 5, "rarity": "uncommon", "weight": 3},
    {"name": "axe", "damage": 12, "rarity": "rare", "weight": 6}
]

for item in chest:
    print(f"- {item['name'].title()} (damage {item['damage']})")
    
choosen_item = input("\nChoose your weapon: ").strip().lower()

while choosen_item not in [item["name"] for item in chest]:
    choosen_item = input("That’s not in the chest. Try again: ").strip().lower()
    
for item in chest:
    if item['name'] == choosen_item:
        hero["inventory"].append(item)
        chest.remove(item)
        print(f"\nYou picked up the {choosen_item}! It’s now in your inventory.")
        break
    
print("\nA wild goblin appears!")

potion = {"name": "Health Potion", "heal": 100, "rarity": "uncommon"}

goblin = {
    "hp": 30,              
    "damage": 5,
    "reward": {
        "xp": 10,
        "gold": 50,
        "item": potion
    }
}

print(f"The goblin has {goblin['hp']} HP and {goblin['damage']} attack damage!")

weapon = hero["inventory"][0]

print(f"\nYou ready your {weapon['name']} (damage {weapon['damage']}).")

while hero["hp"] > 0 and goblin["hp"] > 0:
    action = input("\nDo you ATTACK or RUN? ").strip().lower()
    
    if action == 'run':
        print("You flee the battle. The goblin laughs victoriously...")
        break
    elif action == 'attack':
        goblin["hp"] -= weapon["damage"]
         
        if goblin["hp"] < 0:
            goblin["hp"] = 0
        
        print(f"You strike the goblin! It now has {goblin['hp']} HP left.")
    
        if goblin["hp"] <= 0:
            print("The goblin has been defeated!")
            break
    
        hero["hp"] -= goblin["damage"]
    
        if hero["hp"] < 0:
            hero["hp"] = 0
        
        print(f"The goblin hits back! Your HP: {hero['hp']}")
    else:
        print("Invalid action. Try again!")

print("\nBattle results:")

if hero["hp"] > 0 and goblin["hp"] <= 0:
    print(f"You won! You gain {goblin['reward']['xp']} XP and {goblin['reward']['gold']} gold.")
    
    hero["xp"] += goblin["reward"]["xp"]
    hero["gold"] += goblin["reward"]["gold"]
    
    hero["inventory"].append(goblin["reward"]["item"])
    print("You also found a potion and added it to your inventory.")
else:
    print("You were defeated...")
    print("Maybe you can return for revenge. The chest still contains:")
    for item in chest:
        print(f"- {item['name'].title()}")
         
if hero['xp'] >= 10:
    while hero['xp'] >= 10:
        hero["xp"] -= 10
        hero["level"] += 1
        print(f"Level up! You are now level {hero['level']}")
           
print("\nFinal Hero Stats:")
for key, value in hero.items():
    if key != "inventory":
        print(f"{key}: {value}")

print("\nInventory contains:")
for item in hero["inventory"]:
    print("-", item["name"])

