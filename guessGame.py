import random

print("""
            Guess Game
In this game you will have 10 chances to geuss my number. 
You will be given hints in between to help you out.
            Good Luck
      """)

playAgain = 'y'
while playAgain == 'y':
    
    myNum = random.randint(1,100)

    for i in range(10):
        num = int(input(f'You have {10-i} number of chances remaining:\n'))

        if num > myNum:
            print('Oops! wrong number. Your number is too high.')
        elif num < myNum:
            print('Oops! wrong number. Your number is too low.')
        else:
            print('Yay!! you guessed it correct.\n')
            break
    else:
        print('Game Over... You loose')

    playAgain = input('Do you want to play again?[y/n]\n')

    


