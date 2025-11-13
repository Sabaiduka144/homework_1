def travel_time(distance_km, speed_kmh=5):
    time_hours = distance_km / speed_kmh
    return time_hours

dit_km = int(input("Enter distance in kilometers: "))
speed_kmh = int(input("Enter speed in km/h: "))
time = travel_time(dit_km, speed_kmh)

print(f"You'll be traveling {dit_km}km with a speed of {speed_kmh}km/h and you'll be there in {round(time)} hours")

def format_supplies(water_liters, snacks):
    return f"Pack {water_liters}L of water and {snacks} snacks."

print(format_supplies(3 if dit_km > 100 else 2, 5 if dit_km > 100 else 3))

def create_hero():
    return {
        "name": "Hero",
        "hp": 30,
        "xp": 0,
        "gold": 0,
        "inventory": [],
    }

def create_chest():
    return [
        {"name": "Sword", "damage": 10},
        {"name": "Axe", "damage": 12},
        {"name": "Dagger", "damage": 6},
    ]

def create_goblin():
    return {
        "name": "Goblin",
        "hp": 20,
        "damage": 5,
        "reward": {"xp": 10, "gold": 5, "item": {"name": "Goblin Ear", "type": "trophy"}},
    }
    
def choose_weapon(chest):
    while True:
        print("Available weapons:")
        for i, weapon in enumerate(chest):
            print(f"{i+1}. {weapon['name']} (Damage: {weapon['damage']})")
        choice = input("Choose a weapon by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(chest):
            weapon = chest.pop(int(choice)-1)
            return weapon
        print("Invalid choice, try again.")

def deal_damage(attacker, defender):
    damage = attacker.get("damage", 0)
    defender["hp"] = max(defender["hp"] - damage, 0)
    print(f"{attacker['name']} hits {defender['name']} for {damage} damage!")
    return defender

def is_defeated(character):
    return character["hp"] <= 0

def run_battle(hero, goblin, weapon):
    while True:
        goblin = deal_damage({"name": hero["name"], "damage": weapon["damage"]}, goblin)
        if is_defeated(goblin):
            return "victory"

        hero = deal_damage(goblin, hero)
        if is_defeated(hero):
            return "defeat"
        
def apply_reward(hero, reward):
    hero["xp"] += reward["xp"]
    hero["gold"] += reward["gold"]
    hero["inventory"].append(reward["item"])
    print(f"Victory! You gained {reward['xp']} XP, {reward['gold']} gold, and a {reward['item']['name']}.")

def show_defeat_summary(chest):
    print("You were defeated! Try again.")
    print(f"Remaining items in chest: {[item['name'] for item in chest]}")

def main():
    hero = create_hero()
    chest = create_chest()
    goblin = create_goblin()

    weapon = choose_weapon(chest)
    outcome = run_battle(hero, goblin, weapon)

    if outcome == "victory":
        apply_reward(hero, goblin["reward"])
    else:
        show_defeat_summary(hero, chest)

    print("Final hero stats:", hero)
    print("Inventory items:")
    for item in hero["inventory"]:
        print("-", item["name"])

if __name__ == "__main__":
    main()
