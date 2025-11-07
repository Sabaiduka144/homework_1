import random

number = random.randint(0, 100)
tries = 7

while True:
    guess = int(input("Guess a number between 0 and 100 (or type 'exit' to quit): "))
    tries -= 1
    
    if guess == "exit":
        print("Thanks for playing!")
        break
    if guess < number:
        print("Too low! Try again.")
        continue
    if guess > number:
        print("Too high! Try again.")
        continue
    if guess == number: 
        print("Congratulations! You've guessed the number.")
        break
    if tries < 0:
        print(f"Sorry, you've run out of tries. The number was {number}.")
        break