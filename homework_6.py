import random
from datetime import datetime

def square(number):
    return number ** 2

def shift_and_square(number, offset):
    return square(number + offset)


print("Task 1 Demonstration:")
print("square(5) =", square(5))
print("shift_and_square(3, 2) =", shift_and_square(3, 2))
print()

def check_balance():
    return random.choice([True, False])


def complete_transaction(total=10.0, **kwargs):
    order = {
        "status": "success",
        "order_id": random.randint(1000, 9999),
        "total": total,
        "metadata": kwargs
    }
    print(f"Transaction completed! Order ID: {order['order_id']}")
    return order


def place_order(total=10.0):
    if check_balance():
        return complete_transaction(total=total)
    else:
        return {
            "status": "failed",
            "order_id": None,
            "total": total,
        }


print("Task 2 Demonstration:")
results = []
for i in range(3):
    results.append(place_order())

for i, result in enumerate(results, start=1):
    if result["status"] == "success":
        print(f"Attempt {i}: SUCCESS — Order ID {result['order_id']}, Total: {result['total']}")
    else:
        print(f"Attempt {i}: FAILED — Insufficient balance.")
print()

print("Task 3 Demonstration:")
print("square(4) =", square(4))
print("shift_and_square(5, 3) =", shift_and_square(5, 3))
print()

def safe_place_order(max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        print(f"Safe attempt {attempt}...")
        result = place_order()

        if result["status"] == "success":
            print("Success on attempt", attempt)
            return result

        print("Failed attempt", attempt)

    print("All attempts failed.")
    return None


print("Task 4 Demonstration:")
safe_place_order()
print()

def log(message):
    print(f"[{datetime.now()}] >> {message}")


log("Logger example working.")

def run_tests():
    assert square(3) == 9
    assert shift_and_square(2, 3) == (2 + 3) ** 2
    print("All mini-tests passed!")


run_tests()