#Number Guessing Game 
import random

while True:

    # Random Number
    SecretNum = random.randint(0, 100)

    Attempts = 0
    max_attempts = 7

    print("\nA new game has started!")

    # Game Loop
    while True:
        try:
            Guess = int(input(f"\nAttempt {Attempts + 1}/{max_attempts}: Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        Attempts += 1

        if Guess > SecretNum:
            print("Too High!")

        elif Guess < SecretNum:
            print("Too Low!")

        else:
            print(f"\n🎉 Congratulations! You guessed the number in {Attempts} attempts.")
            break

        # Hint after 4 attempts
        if Attempts == 4:
            if SecretNum % 2 == 0:
                print("Hint: The secret number is EVEN.")
            else:
                print("Hint: The secret number is ODD.")

        # Game Over
        if Attempts >= max_attempts:
            print(f"\nGame Over! Better luck next time.")
            print(f"The secret number was {SecretNum}.")
            break

    # Play Again
    choice = input("\nDo you want to play again? (yes/no): ")

    if choice != "yes":
        print("\nThanks for playing! Have a nice day. 😊")
        break


     
