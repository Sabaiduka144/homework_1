name = "Saba"
age = "15"
has_coded_bef = True

print("***************")
print("Name:", name)
print("Age:", age)
print("Has coded before?", "Yes" if has_coded_bef else "No")
print("***************")

num1 = int(input("Input number: "))
num2 = int(input("Input another number: "))

print("***************")
print("+:", num1 + num2)
print("-:", num1 - num2)
print("*:", num1 * num2)
print("/:", num1 / num2)
print("Is first greater than second?", num1 > num2)
print("Is first less than second?", num1 < num2)
print("Are they equal?", num1 == num2)
print("***************")

minutes = int(input("Enter a minute: "))
hours = minutes / 60
print(minutes, "minute equals to ", hours, "hours")



print("***************")
height = int(input("Insert your height: "))
weight = int(input("Insert your weight: "))
age = int(input("Insert your age: "))

bmr = 10 * weight + 6.25 * height - 5 * age + 5
dci = bmr * 1.5

print("***************")
print("Your daily calorie intake should be:", round(dci))
print("To gain weight:", round(dci + 500))
print("To lose weight", round(dci - 500))
print("***************")