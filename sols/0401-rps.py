import random

def get_p1_move():
    choice = None
    while choice != "r" and choice != "p" and choice != "s":
        choice = input("Enter your move from [r|p|s]: ").lower()
    return choice

def get_rounds():
    choice = -1
    while choice < 0 or choice > 9:
        choice = int(input("Enter the number of rounds to play, from 1 to 9: "))
    return choice

def get_comp_move():
    choice = random.randint(1,3)
    if choice == 1:
        return "r"
    elif choice == 2:
        return "p"
    else:
        return "s"

# returns p, c, or tie based on winner
def get_round_winner(p1move, cmove):
    if p1move == cmove:
        return "tie"
    elif    (p1move == "r" and cmove == "p") or \
            (p1move == "p" and cmove == "s") or \
            (p1move == "s" and cmove == "r"):
        return "c"
    else:
        return "p"

def move(short):
    if short == "r":
        return "Rock"
    elif short == "p":
        return "Paper"
    else:
        return "Scissors"

def print_score(pscore,cscore,ties):
    print("Player Wins: {}".format(pscore))
    print("Computer Wins: {}".format(cscore))
    print("Ties: {}".format(ties))
    

def rps():
    print("Welcome to Rock Paper Scissors!")
    rounds = get_rounds()
    pscore = 0
    cscore = 0
    ties = 0
    for r in range(rounds):
        print("-----------------")
        print("Round {}!".format(r+1))
        p1move = get_p1_move()
        cmove = get_comp_move()
        winner = get_round_winner(p1move, cmove)
        
        print("You picked: {}\nComputer picked: {}".format( move(p1move), move(cmove) ))
        
        if winner == "tie":
            print("It's a tie!")
            ties = ties + 1
        elif winner == "c":
            print("Computer won!")
            cscore = cscore + 1
        else:
            print("Player won!")
            pscore = pscore + 1
        
        print_score(pscore,cscore,ties)
        
        if pscore > rounds/2 or cscore > rounds/2:
            break
    
    if pscore > cscore:
        print("The player is victorious! P:{} to C:{}!".format(pscore,cscore) )
    elif pscore == cscore:
        print("Everyone tied! P:{} to C:{}!".format(pscore,cscore) )
    else:
        print("The computer is victorious! P:{} to C:{}!".format(pscore,cscore) )

if __name__ == "__main__":
    rps()