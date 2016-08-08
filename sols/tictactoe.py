def move_is_valid(move, board):
    if not move.isdigit(): # move is not a number 
        return False
    
    move = int(move)
    
    if move < 1 or move > 9: # is out of bounds
        return False
    elif board[move-1] != move: # pos is not a number (taken)
        return False
    return True
        
def get_move(player, board):
    move = input("Player {}, enter your move as a number from 1 to 9: ".format(player))
    
    while not move_is_valid(move, board): 
        print("Invalid input, try again")
        move = input("Player {}, enter your move as a number from 1 to 9: ".format(player))
    
    board[int(move)-1] = player
    
def print_board(board):
    print()
    print(" {} | {} | {}".format(board[0],board[1],board[2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[3],board[4],board[5]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[6],board[7],board[8]))
    print()

def is_over(board):
    for pos in board:
        if pos != "X" and pos != "Y":
            return False
    return True

def player_won(board):
    wins = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
           ]
    
    for w in wins:
        if board[w[0]] == board[w[1]] and \
           board[w[0]] == board[w[2]]:
            return w[0]
    return "no"

def swap_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

def ttt():
    board = [1,2,3,4,5,6,7,8,9]
    player = "X"
    
    while not is_over(board):
        print_board(board)
        get_move(player, board)
        if player_won(board) != "no":
            break
        player = swap_player(player)
    
    print_board(board)
    print("Tic Tac Toe, 3 in a row!")
    print("Player {} wins!".format(player))
    
if __name__ == "__main__":
    ttt()