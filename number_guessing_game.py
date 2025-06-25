import random


# Generate a random number between 1 and 100
def guessing_game():
    random_num = random.randint(1, 101)

    # Numeber of chances
    chances = 0  # Store the number of guesses

    while True:  # Create a loop where it runs until the user guess the correct number
        try:  # Create an exception to guarantee the user type just numbers

            guess = input("Guess a number: ")
            guess = int(guess)
            if chances == 3:  # GIve just 3 guesses
                print("You are out of chances.")
                break
            elif guess > random_num:
                print("Too high")
                chances += 1
            elif guess < random_num:
                print("Too low")
                chances += 1
            else:
                print("Just Right")
                break

        except ValueError:
            print("You should use a valid number.")


guessing_game()
