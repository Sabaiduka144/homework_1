import time
unprinted_designs = ["Phone case", "Shirt", "Cup"]
completed_designs = []

while unprinted_designs:
    just_printed = unprinted_designs.pop()
    print(f"Just Printed {just_printed}")
    completed_designs.append(just_printed)
    time.sleep(1)
    
for design in completed_designs:
    print(f"Completed Design: {design}")
    time.sleep(1)

def make_pizza(size, **toppings):
    print(f"Make {size}-Size Pizza With The Following Ingredients: ")
    for key, topping in enumerate(toppings):
        print(f"{key + 1}. {topping}")
        time.sleep(1)
    
make_pizza(16, meat="peperonni", cheese="chedar", tomatos="tomatoes")

cars = [
    {"brand": "Subaru", "model": "Outback", "color": "Blue"},
    {"brand": "Subaru", "model": "Forester", "color": "Blue"},
    {"brand": "BMW", "model": "X5", "color": "Black"},
    {"brand": "BMW", "model": "M5", "color": "Black"},
    {"brand": "Toyota", "model": "Corolla", "color": "White"},
    {"brand": "Honda", "model": "Civic", "color": "Red"}
]

def find_car(brand):
    brand = brand.title()

    matches = []
    for car in cars:
        if car["brand"] == brand:
            matches.append(car)


    if not matches:
        print("No cars found.")
        return

    for car in matches:
        print("Finding...")
        time.sleep(2.3)
        print(f"Found Car: {car['brand']} {car['model']} (Color: {car['color']})")

    print(f"Completed in {2.3 * len(matches)} seconds")
find_car("subaru")