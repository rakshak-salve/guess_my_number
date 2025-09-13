import random  # I heard this is how you get random numbers in Python

print("Hi! Let's play a guessing game.")
print("I'm thinking of a number from 1 to 100.")

# Not sure if there's a better way, but this worked for me!
secret_number = random.randint(1, 100)
tries = 0  # I want to count how many guesses it takes

while True:
    try:
        # Get the user's guess (as a number)
        user_guess = int(input("Your guess: "))
        tries += 1  # Add 1 every time they guess
        if user_guess < secret_number:
            print("Nope, too low. Try again!")
        elif user_guess > secret_number:
            print("Nope, too high. Try again!")
        else:
            print(f"Yay! You got it in {tries} tries.")
            break  # This ends the game
    except ValueError:
        # This happens if they type something that's not a number
        print("Oops, that wasn't a number. Enter a number between 1 and 100.")
# I hope this works! Still learning Python :)
