import random

def guess_the_number():
    print('\nWelcome to Guess the Number! :)')
    number = random.randint(1, 50)
    attempts = 7

    while attempts > 0:
        try:
            guess = int(input('Please make a guess of any number from 1 to 50:\nYour guess: '))
        except ValueError:
            print('Please enter a whole number.')
            continue

        if guess < 1 or guess > 50:
            print('Please type a number between 1 and 50.')
            continue

        if guess == number:
            print("🎉 Congratulations! You win! :)")
            break
        elif guess > number:
            print("Too high! Try again!")
        else:
            print("Too low! Try again!")

        attempts -= 1
        print(f'Attempts left: {attempts}')

    else:
        print(f"Out of guesses. The number was {number}. Try again!")

def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    print("\nWelcome to Rock, Paper, Scissors! :)")

    while True:
        computer_choice = random.choice(options)
        player_choice = input('Please choose between rock, paper, or scissors:\n').lower()

        if player_choice not in options:
            print("Please type rock, paper, or scissors.")
            continue

        print(f"\nComputer chose: {computer_choice}")

        if computer_choice == player_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print('Player wins!')
        else:
            print("Computer wins!")

        play_again = input("\nWould you like to play again? Type (Y/N):\n").lower()
        if play_again != 'y':
            print("Thank you for playing :)")
            break

#Main Menu
while True:
    print("\n Welcome to Pirate Games!")
    print("1. Guess the Number")
    print("2. Rock Paper Scissors")
    print("3. Exit")

    choice = input("Please choose a game to play. 1 for Guess the Number and 2 for Rock Paper Scissors. 3 to exit: ")

    if choice == '1':
        guess_the_number()
    elif choice == '2':
        rock_paper_scissors()
    elif choice == '3':
        print("Thank you for checking out Pirate Games! Come back soon! :)")
        break
    else:
        print("Choice is not valid. Please choose 1, 2, or 3.")