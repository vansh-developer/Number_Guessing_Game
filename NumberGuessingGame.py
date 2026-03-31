import random
def number_guessing_game():
    computer_choice = random.randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("I have chosen number from 1 to 100. Guess it!")
    attempt = 0
    while True:
        try:
            user_choice = int(input("Enter your guess: "))
        except ValueError:
            print("Error: Enter numbers only.")
            continue
        attempt += 1
        if(attempt == 10):
            print(f"Game Over! The number was taken by {computer_choice}.")
        if (user_choice > computer_choice):
            print("Too high! Try again!")
        elif (user_choice < computer_choice):
            print("Too low! Try again!")
        else:
            print(f"Congratulations! You have guessed {computer_choice} correctly. It took you {attempt} attempts to complete it.")
            break
number_guessing_game()
