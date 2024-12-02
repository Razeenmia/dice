import random

# Function to simulate rolling a dice
def roll_dice():
    return random.randint(1, 6)

# Function to start the dice rolling game
def start_game():
    while True:
        print("Welcome to the Dice Rolling Simulator!")
        print("Press 'r' to roll the dice, or 'q' to quit the game.")

        # Taking user input for roll or quit
        user_input = input("Enter your choice: ").lower()

        # If user chooses to roll the dice
        if user_input == 'r':
            roll = roll_dice()
            print(f"You rolled a {roll}!")
        # If user chooses to quit the game
        elif user_input == 'q':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'r' to roll or 'q' to quit.")

# Call the function to start the game
start_game()
