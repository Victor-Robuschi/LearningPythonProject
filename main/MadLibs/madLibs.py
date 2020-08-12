import os.path

# print out a welcome massage
print('Hi and welcome to Vic\'s Mad Libs!')

# print out instructions to the game
input('Press enter to continue')

# ask for input*4
print('You are gonna be ask for 3 words')

# Save word in 4 str
verb = input('4. Write a verb: ')
noun = input('3. Write a noun: ')
adjective = input('2. Write a adjective: ')
adverb = input('1. Write a adverb: ')

# The mad labs in question
madLibs = '''The day I saw the Monkey King {} was one of the most
interesting days of the year. After he did that, 
the king played chess on his brother's {} and then combed his {} hair with a
comb made out of old fish bones. Later that same day, I saw the
Monkey King dance {} in front of an audience of kangaroos and wombats.'''

# print out the MadLib
print(madLibs.format(verb, noun, adjective, adverb))

# ask to save to a file
userInput = input('Would you like to save your mad lib\'s in a text file? y/n: ').upper()

# create file and write the mad libs in to the file and save to desktop
if userInput == 'Y':
    nameOf_TheFile = input('Enter the name of the file: ')
    path = "C:/Users/victo/Desktop"
    fileName = nameOf_TheFile
    fileNameAndPath = os.path.join(path, fileName + '.txt')
    madLibsTxt = open(fileNameAndPath, 'w')
    madLibsTxt.write(madLibs.format(verb, noun, adjective, adverb))
    madLibsTxt.close()

# Error! text contains {} instead of the saved words. SOLVED! .format with parameters

print('Thank you for playing Vic\'s Mad Lib\'s!')
print('Have a nice day!')