import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

# rules to determine who wins the game
    if user == computer:
        return 'It\'s a tie'
    
    # in this game we know;
    # r > s, p > r, s > p
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'  # when the computer wins

# helper function to determine who wins the game
def is_win(player, opponent):
    #return true if player wins, false if not
    # r > s, p > r, s > p

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    

print(play())