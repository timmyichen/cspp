""" pseudocode

create the solution by RNG
set number of guesses to 0
make user incorrect by default
then while the user is incorrect:
    ask the user for a guess
    increase the number of guesses by 1
    if the guess is greater than solution, that means the user's guess is too high.  tell the user that
    if the guess is less than the solution, that means the user's guess is too low.  tell the user that
    if the guess is right, then it will quit out of the loop
if we hit this point, it means the user was right.  congratulate them!
report the number of guesses to the user

"""
import random
    
def main():
    answer = random.randint(1,100)
    guess_count = 0
    guess = -1
    while guess != answer:
        guess = int(input("Enter your guess (1-100): "))
        guess_count = guess_count + 1;
        if guess > answer:
            print("Too high! Try again.")
        elif guess < answer:
            print("Too low! Try again.")
    
    print("You got it! It was indeed {}. It took you {} tries. You're like the best person ever.".format(answer, guess_count))
    
main()