import random
import art

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    number = random.randint(0,100)

    difficulty_chosen = input("Type 'easy' or 'hard' : ")

    lives = 0

    if difficulty_chosen == "easy":
        lives = 10
    elif difficulty_chosen == "hard":
        lives = 5

    lives_exist = True
    guessed = False

    print(f"Amount of lives {lives}")
    print(f"Psst the correct answer is {number}")

    while lives_exist:
        guess = int(input("Guess the number: "))
        if guess > number :
            print(f"Too high, guess something lower than {guess}")
            lives = lives - 1 # remember python has no block scope!
            print(f"Amount of lives left {lives}")
            if lives == 0:
                lives_exist = False
                print("Womp womp, Failed!")

        elif guess < number :
            print(f"Too low, guess something higher than {guess}")
            lives = lives -1
            print(f"Amount of lives left {lives}")
            if lives == 0:
                lives_exist = False
                print("Womp womp, Failed!")

        elif guess == number:
            print(f"Correct! {guess} is the number!")
            break

    play_again = input("Do you want to still play? type y/n: ").lower()
    if play_again == "y":
        game()

game()