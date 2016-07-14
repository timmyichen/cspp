import random

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("The dice is thrown: {} and {}, {} total".format(dice1,dice2,dice1+dice2))
    return dice1+dice2

def get_bet(bank):
    print("You have ${} in your bank".format(bank))
    bet = -1
    while bet < 0 or bet > bank or bet != int(bet):
        bet = float(input("Enter a whole number for your bet: "))
        if bet < 0:
            print("You can't bet negative money!")
        elif bet > bank:
            print("You don't have that much money!")
        elif bet != int(bet):
            print("You need to bet an integer amount!")
    return bet

def wait_for_user():
    input("Press enter to continue.")
    
#returns 1 if win
#returns -1 if loss
#returns sum of roll if point number chosen
def first_roll():
    roll = roll2dice()
    if roll == 2 or roll == 3 or roll == 12:
        print("You rolled a {} on first roll! You lose the round!".format(roll))
        return -1
    elif roll == 7 or roll == 11:
        print("You rolled a {} on first roll! You win the round!".format(roll))
        return 1
    else:
        return roll

#returns 1 if win
#returns -1 if loss
#returns 0 if reroll
def point_roll(point_num):
    roll = 0
    while(roll != 7 and roll != point_num):
        roll = roll2dice()
        if roll == 7:
            print("You rolled a 7! You lose the round!")
            return -1
        elif roll == point_num:
            print("You rolled your point number!  You win the round!")
            return 1
        else:
            print("No 7 or {}.  Reroll!".format(point_num))
        wait_for_user()

def get_bank_value(bet,bank,result):
    if result == 1:
        return bank + bet
    else:
        return bank - bet

def keep_playing(bank):
    choice = None
    while choice != "y" and choice != "n":
        choice = input("Do you want to keep playing? [y|n]: ").lower()
        if choice == "y":
            return True
        else:
            return False

def print_end_message(bank):
    if bank == 0:
        print("You lost everything!  Sorry, better luck next time!")
    else:
        print("Looks like you made it out with {}! Not bad.".format(bank))

def craps():
    bank = 100
    play = True
    while play and bank > 0:
        bet = get_bet(bank)
        result = first_roll()
        if result == 1 or result == -1:
            bank = get_bank_value(bet,bank,result)
        else:
            print("Your point number is {}".format(result))
            wait_for_user()
            result = point_roll(result)
            bank = get_bank_value(bet,bank,result)
        
        if bank != 0:    
            play = keep_playing(bank)

    print_end_message(bank)
    
if __name__ == "__main__":
    craps()