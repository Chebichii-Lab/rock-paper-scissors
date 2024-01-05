import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

# rules to determine who wins the game
    if user == computer:
        return 'tie'
    
    # in this game we know;
    # r > s, p > r, s > p


    