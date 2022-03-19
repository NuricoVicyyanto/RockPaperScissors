import random

user_actions = ['rock', 'paper', 'scissors']

action = input('Rock, paper, scissors? ')
computer_action = random.choice(user_actions)

print('You chose:', action, 'and the computer chose:', computer_action)

if action == computer_action:
    print('Tie!')
elif action == 'rock' and computer_action == 'paper':
    print('You lose!')
elif action == 'rock' and computer_action == 'scissors':
    print('You win!')
elif action == 'paper' and computer_action == 'rock':
    print('You win!')
elif action == 'paper' and computer_action == 'scissors':
    print('You lose!')
elif action == 'scissors' and computer_action == 'rock':
    print('You lose!')
elif action == 'scissors' and computer_action == 'paper':
    print('You win!')
else:
    print('Invalid action!')