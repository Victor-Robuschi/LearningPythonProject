

# print out a welcome massage
print('Hi and welcome to Vic\'s Number Guesser!')
input('Press enter to continue')

# ask to print out instructions to the game
user_rules_input = input('would you like to know the rules of the game? y/n: ').upper()

# print out instructions
if user_rules_input == 'Y':
    print('''The name of the game is to guess a number between 0 and a choosen number.
    Then you will be ask how many guesses you will limit yourself with.
    If your guess is higher or lower then the right number you'll be given a hint.
    You WIN if you guess the right number before you go over the number of guesses you have, 
    otherwise you LOSE!''')
    player_ready_input = input('\nAre you ready to play?(N = program will close)  y/n').upper()
    if player_ready_input == "N":
        print('Program exit')
        exit()


