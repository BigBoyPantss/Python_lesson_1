import random #python libraries are set of functions so you dont write a code from scratch

def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors) ')
    options = ["rock", "paper", "scissors"] #list 
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice} # dictionary
    return choices 

def check_win(player, computer):
    print(' You chose ' + player + ", computer chose " + computer)
    if player == computer:
        return "its a tie"
    elif player == 'rock':
        if computer == 'paper':
            return 'Paper eats rock'
        else:
            return 'rock beats scissor'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper eats rock'
        else:
            return 'scissor beats paper'
    
    elif player == 'scissor':
        if computer == 'rock':
            return 'rock beats scissor'
        else:
            return 'scissor beats paper' 
     
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)