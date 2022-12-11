import random
import os

diceValues = [1, 2, 3, 4, 5, 6]
diceASCII = ['NULL', '-----\n|   |\n| o |\n|   |\n-----', '-----\n|o  |\n|   |\n|  o|\n-----', '-----\n|o  |\n| o |\n|  o|\n-----', '-----\n|o o|\n|   |\n|o o|\n-----', '-----\n|o o|\n| o |\n|o o|\n-----', '-----\n|o o|\n|o o|\n|o o|\n-----']

# function that prints dice according to the given value
def printDice(value):
    print(diceASCII[value])

# main
rollAgain = True
while rollAgain:
    os.system('cls')
    print('DICE SIMULATOR\n')
    diceVal = random.choice(diceValues)
    printDice(diceVal)
    roll = input('\n\nRoll Dice Again? (Y or N): ')[0]
    if roll == 'Y' or roll == 'y':
        continue
    else:
        rollAgain = False

