def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return 'win'
    else:
        return 'lose'