import random

# print out a welcome massage
print('Hi and welcome to Vic\'s Number Guesser!')
input('Press enter to continue')

# ask to print out instructions to the game
user_rules_input = input('would you like to know the rules of the game? y/n: ').upper()

# print out instructions
if user_rules_input == 'Y':
    print('''The name of the game is to guess a number between 0 and a player chosen number.
    Then you will be ask how many guesses you will limit yourself with.
    If your guess is higher or lower then the right number you'll be given a hint.
    You WIN if you guess the right number before you go over the number of guesses you have, 
    otherwise you LOSE!''')
    player_ready_input = input('\nAre you ready to play?(N = program will close)  y/n: ').upper()
    if player_ready_input == "N":
        print('Program exit')
        exit()
# ask for the range of number to be guessed
number_range = int(input("Please choose the guessing range, enter a number higher then 0: "))

# ask for number of guesses user will have to guess right
numberOf_guesses = int(input("Please enter the number of guesses you will have: "))

# have code pick a number
computer_picked_number = random.randrange(0, number_range)

# for testing purpose: print(computer_picked_number)

# bool to help control while loop
run_game = True

# user get 'numberOf_guesses' chances to guess (loop)
# user guess the number
while numberOf_guesses > 0 and run_game == True:
    user_guess = int(input("Guess: "))

# compare the user guess to computer picked number
    if user_guess != computer_picked_number: # WRONG GUESS
        # give user hint if guess is less then or more then
        if user_guess > computer_picked_number:
            print("Wrong number! please try a lower number")
        if user_guess < computer_picked_number:
            print("Wrong number! please try a higher number")
        numberOf_guesses -= 1

# if guessed right print victory massage
    elif user_guess == computer_picked_number:
        run_game = False
        print("YOU GUESSED RIGHT!!")
        print("Good job, Have a nice day!")

# if guessed wrong more times then 'user_max_guesses' print losing massage
if numberOf_guesses == 0:
    print("You ran out of guesses, you suck.")
    print("bye")

# print exit massage
print("program exit")
