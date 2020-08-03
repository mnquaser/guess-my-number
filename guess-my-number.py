#I tried to replicate the game from the introduction page from page 35 of the book
import random


def myNum():
    my_num = random.randint(5, 85)
    print("I am thinking of a number, guess the number I am thinking of : ", end="")
    while True:
        try:
            guess = int(input())
            if guess == my_num:
                print("That's it! Would you like to play again? ", end="")
                while True:
                    decision = input("(yes/no) ").casefold()
                    try:
                        if decision == "yes":
                            return myNum()
                        elif decision == "no":
                            print("Thanks for playing!")
                            break   # THere is a bug which needs to be fix. it adds a newline before breaking.
                        else:
                            raise ValueError
                    except ValueError:
                        print("Please type 'yes' to play again, and 'no' to stop the game! ", end="")
                        continue
            elif guess > my_num:
                print("Too high! Guess again : ", end="")
                continue
            elif guess < my_num:
                print("Too low! Guess again : ", end="")
                continue
        except ValueError:
            print("Please enter an integer value! Try again : ", end="")
            continue


myNum()
