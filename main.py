import random

# def game
game = ['R', 'P', 'S']

# input validation
while True:
    userInput = input('pick between R,P,or S \n').upper()
    computerChoice = random.choice(game)
    if userInput not in game:
        print('not an option')
    
    else:
        print(f"Player ({userInput}) : CPU ({computerChoice})")
        if userInput == computerChoice:
            pass
        else :
            if userInput == 'R' and computerChoice == 'P':
                print('Computer Wins')
            elif userInput == 'P' and computerChoice == 'R':
                print('You win')

            if userInput == 'R' and computerChoice == 'S':
                print('You win')
            elif userInput == 'S' and computerChoice == 'R':
                print('Computer Wins')

            if userInput == 'P' and computerChoice == 'S':
                print('Computer Wins')
            elif userInput == 'S' and computerChoice == 'P':
                print('You win')

            # print(f"Player ({userInput}) : CPU ({computerChoice})")
            break
