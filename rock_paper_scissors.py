import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

# rules to determine who wins the game
    if user == computer:
        return 'tie'
    
    # in this game we know;
    # r > s, p > r, s > p

# helper function to determine who wins the game
def is_win(player, opponent):
    #return true if player wins, false if not
    # r > s, p > r, s > p

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True