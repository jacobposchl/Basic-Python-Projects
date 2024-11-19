import random
min_val, max_val = 1, 10
random_int = random.randint(min_val, max_val)


def check_number(num):
    if num == random_int:
        print("CORRECT! YOUR GUESS WAS ", num, "THE CORRECT ANSWER WAS ", random_int)
    else:
        print("INCORRECT! TRY AGAIN")
        guess_number()
4
def guess_number():
    guessed_int = int(input(f"Guess a number from {min_val} to {max_val}: "))
    check_number(guessed_int)

guess_number()

