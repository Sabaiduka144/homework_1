name = "Saba"
age = "15"
has_coded_bef = True
fav_lang = "Python"

print("***************")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Has coded before? {'Yes' if has_coded_bef else 'No'}")
print(f"Favorite programming language: {fav_lang}")
print("***************")

num_1 = int(input("Input number: "))
num_2 = int(input("Input another number: "))

print("***************")
print(f"\nComparing strings: '{num_1}' > '{num_2}' = {num_1 > num_2}")
print("***************")

num1 = int(num_1)
num2 = int(num_2)

print(f"+: {num1 + num2}")
print(f"-: {num1 - num2}")
print(f"*: {num1 * num2}")
print(f"/: {num1 / num2}")
print(f"Is first greater than second? {num1 > num2}")
print(f"Is first less than second? {num1 < num2}")
print(f"Are they equal? {num1 == num2}")
print("***************")

minutes = int(input("Enter the number of study minutes completed today: "))
hours = minutes // 60
remaining = minutes % 60
print(f"You studied for {hours} hours and {remaining} minutes today. Great job!")

energy = int(input("On a scale of 1-5, what is your current energy level? "))

if energy >= 4 and energy <= 5:
    print("Keep working")
elif energy == 3:
    print("You might want to take a short break.")
elif energy <= 2:
    print("You should take a longer rest.")
else:
    print("That number isn’t on the 1–5 scale. Try again!")
    
if minutes > 180 and energy >= 4:
    print("Packed study schedule!")