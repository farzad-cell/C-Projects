import random

print('\nWelcome to RPS GAME. Enter your choice: \n0-Exit\n1-Rock\n2-Paper\n3-Scissors\n')


while True:

    try:
        player = int(input())
    except ValueError:
        print('Invalid choice. Please try again.')
        continue
    if player not in [1,2,3,0]:
        print('Please enter a valid choice.')
        continue

    if player == 0:
        print('Thank you for playing!')
        break

    x = random.randint(1,3)

    if x == 1:
        if player == 1:
            print('You: Rock')
            print('Computer: Rock')
            print('Tie')
        elif player == 2:
            print('You: Paper')
            print('Computer: Rock')
            print('You Won!')
        elif player == 3:
            print('You: Scissors')
            print('Computer: Rock')
            print('You Lost:(')

    elif x == 2:
        if player == 1:
            print('You: Rock')
            print('Computer: Paper')
            print('You Lost:(')
        elif player == 2:
            print('You: Paper')
            print('Computer: Paper')
            print('Tie')
        elif player == 3:
            print('You: Scissors')
            print('Computer: Paper')
            print('You Won!')

    elif x == 3:
        if player == 1:
            print('You: Rock')
            print('Computer: Scissors')
            print('You Won!')
        elif player == 2:
            print('You: Paper')
            print('Computer: Scissors')
            print('You Lost:(')
        elif player == 3:
            print('You: Scissors')
            print('Computer: Scissors')
            print('Tie')
