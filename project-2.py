import random

target_number = random.randint(1,100)
correctly_gussed = False

attempts = 0

print("Guess a number between 1 and 100")

while not correctly_gussed:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > target_number:
            print("Your guess is too high")
        elif guess < target_number:
            print("Your guess is too low")
        else:
            correctly_gussed = True
            print(f"You've guessed the number in {attempts} attempts!")

    except ValueError:
        print("Please enter a numeric value")