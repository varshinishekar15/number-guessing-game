import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("=== Number Guessing Game ===")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
