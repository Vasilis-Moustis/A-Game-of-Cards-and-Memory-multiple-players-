#########################################################################

#First things first, we need a deck.
#Like  every programmer, we seek for the easiest way possible
#We sure can do the [[..], [..], ....] thing but this looks wayy cleaner

#########################################################################
################## D E C K   C R E A T I O N ############################
import itertools
import random
import numpy as np
import array
import time
import os

symbols=['♥','♦','♣','♠']
specials = ['10','J', 'Q', 'K']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9']
scorings = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]

easyVals = ['10', 'jack', 'queen', 'king']
easyVals2 = ['10', 'J', 'Q', 'K']

normalVals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'ace']
normalVals2 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A']

Vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
Vals2 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
Suits = ['spades', 'clubs', 'hearts', 'diamonds']

easydeck = list(itertools.product(easyVals, Suits))
normaldeck = list(itertools.product(normalVals, Suits))
deck = list(itertools.product(Vals, Suits))
worthings = list(itertools.product(Vals, scorings))

'''
random.shuffle(easydeck)
random.shuffle(normaldeck)
random.shuffle(deck)
'''

'''
We can test print our deck with the following
for val, suit in deck:
    print('The %s of %s' % (val, suit))
'''

#########################################################################
############### S E C O N D A R Y   F U N C T I O N S  ##################

def gameDeck(playStyle):
    if playStyle == 1 :
        mydeck = list(itertools.product(easyVals2, symbols))
        random.shuffle(mydeck)
        for i in range (0,4):
            print("\n")
            for j in range (0,4):
                print(mydeck[i*4 +j][0], end="", flush=True)
                print(mydeck[i*4 + j][1], end = "\t", flush=True)
        time.sleep(3)
    elif playStyle == 2:
        mydeck = list(itertools.product(normalVals2, symbols))
        random.shuffle(mydeck)
        for i in range (0,4):
            print("\n")
            for j in range (0,10):
                print(mydeck[i*4 +j][0], end="", flush=True)
                print(mydeck[i*4 + j][1], end = "\t", flush=True)
        time.sleep(3)
    elif playStyle == 3:
        mydeck = list(itertools.product(Vals2, symbols))
        random.shuffle(mydeck)
        for i in range (0,4):
            print("\n")
            for j in range (0,13):
                print(mydeck[i*4 +j][0], end="", flush=True)
                print(mydeck[i*4 + j][1], end = "\t", flush=True)
        time.sleep(3)
    return mydeck

def gameTable(playStyle):
    x,y = 0,0
    if playStyle == 1 :
        x,y = 4,4
    elif playStyle == 2:
        x,y = 4,10
    elif playStyle == 3:
        x,y = 4,13
    return ['X' for i in range(y*x)]

def checkSimilarValues(playStyle, bonusPoints, myDeck, myTable):
    for i in len(myDeck):
        if myTable[i] != 'X':
            for k in range (i+1 , len(myDeck)):
                if myDeck[k][0] == myDeck[i][0] and myTable[i] != 'X':
                    return True
    return False

def checkSimilarSymbols(playStyle, bonusPoints, myDeck, myTable):
    for i in len(myDeck):
        if myTable[i] != 'X':
            for k in range (i+1 , len(myDeck)):
                if myDeck[k][1] == myDeck[i][1] and myTable[i] != 'X':
                    return True
    return False

def checkGameProgress(myTable):
    counter = 0
    for value in myTable:
        if value = 'X':
            counter ++
    if counter < 2 :
        return False
    else:
        return True

def printCurrentOpportunities(myTable):
    if playStyle == 1 :
        for i in range (0,4):
            print("\n")
            for j in range (0,4):
                print('X', end = "\t", flush=True)
    elif playStyle == 2:
        for i in range (0,4):
            print("\n")
            for j in range (0,10):
                print('X', end = "\t", flush=True)
    elif playStyle == 3:
        for i in range (0,4):
            print("\n")
            for j in range (0,13):
                print('X', end = "\t", flush=True)
#########################################################################
##################### G A M E  F U N C T I O N S  #######################
def checkPotentialPoints(playStyle, bonusPoints, myDeck, myTable):
    if bonusPoints:
        return checkSimilarValues(playStyle, bonusPoints, myDeck, myTable) and checkSimilarSymbols(playStyle, bonusPoints, myDeck, myTable)
    else:
        return checkSimilarValues(playStyle, bonusPoints, myDeck, myTable)

def checkKings(s1, s2, myDeck,myTable):
    if myDeck[s1][0] in specials and myDeck[s2][0] in specials:
        if myDeck[s1][0] == 'K' and myDeck[s2][0] = 'K':
            print("You won another pick!")
            return True
    return False

def checkJacks(s1, s2, myDeck,myTable):
    if myDeck[s1][0] in specials and myDeck[s2][0] in specials:
        if myDeck[s1][0] == 'J' and myDeck[s2][0] = 'J':
            print("You won another round!")
            return True
    return False

def checkThirdDrawPotential(sum1, sum2, myDeck, myTable):
    if myDeck[s1][0] in specials and myDeck[s2][0] in specials:
        if myDeck[s1][0] == 'Q' and myDeck[s2][0] = 'J':
            print("You won another chance!")
            return True
        elif myDeck[s1][0] == 'J' and myDeck[s2][0] = 'Q':
            print("You won another chance!")
            return True
    return False

def checkPoints(sum1, sum2, sum3, myDeck, myTable):
    added1, added2, added3 = False, False, False
    score = 0
    for matches in worthings:
        if matches[0] == myDeck[sum1][0] and not added1:
            score += matches[1]
            added1 = True
        if matches[0] == myDeck[sum2][0] and not added2:
            score += matches[1]
            added2 = True
        if sum3 == -1: and matches[0] == myDeck[sum3][0] and not added3:
            score += matches[1]
            added3 = True
    return score

def gameON(playStyle, bonusPoints, ai, players, myDeck, myTable):
    currentPlayer = 0
    line, column = -1,-1
    mline, mcolumn = 4,0
    sum1,sum2,sum3 = 0,0,0
    if playStyle == 1 :
        mcolumn  = 4
    elif playStyle == 2:
        mcolumn = 10
    elif playStyle == 3:
        mcolumn = 13
    while checkGameProgress(playStyle, myTable):
        os.system("clear")
        printCurrentOpportunities(myTable)
        while True:
            while True:
              line = input("Player " + str(currentPlayer + 1) + " choose line number")
              if int(line) > 0 and int(line) <= mline:
                  break
            while True:
              column = input("Player " + str(currentPlayer + 1) + " choose column number")
              if int(column) > 0 and int(column) <= mcolumn:
                  break
            sum1 = line * 4 - 4 + column -1
            if myTable[sum1] == 'X':
                break
            else:
                print("This card has already been flipped")
        print("You draw " + myDeck[sum1][0] + myDeck[sum1][1])
        while True:
            while True:
              line = input("Player " + str(currentPlayer + 1) + " choose line number")
              if int(line) > 0 and int(line) <= mline:
                  break
            while True:
              column = input("Player " + str(currentPlayer + 1) + " choose column number")
              if int(column) > 0 and int(column) <= mcolumn:
                  break
            sum2 = line * 4 - 4 + column - 1
            if myTable[sum2] == 'X':
                break
            else:
                print("This card has already been flipped")
        print("You draw " + myDeck[sum2][0] + myDeck[sum2][1])
        if checkKings(sum1, sum2, myDeck, myTable):
            scorings[currentPlayer] += checkPoints(sum1, sum2, -1, myDeck, myTable)
            currentPlayer += 2
        elif checkJacks(sum1, sum2, myDeck, myTable):
            scorings[currentPlayer] += checkPoints(sum1, sum2, -1, myDeck, myTable)
        elif checkThirdDrawPotential(sum1, sum2, myDeck, myTable):
            while True:
                while True:
                  line = input("Player " + str(currentPlayer + 1) + " choose line number")
                  if int(line) > 0 and int(line) <= mline:
                      break
                while True:
                  column = input("Player " + str(currentPlayer + 1) + " choose column number")
                  if int(column) > 0 and int(column) <= mcolumn:
                      break
                sum3 = line * 4 - 4 + column -1
                if myTable[sum3] == 'X':
                    break
                else:
                    print("This card has already been flipped")
            print("You draw " + myDeck[sum1][0] + myDeck[sum1][1])
            scorings[currentPlayer] += checkPoints(sum1, sum2, sum3, myDeck, myTable)
            currentPlayer += 1
        else:
            scorings[currentPlayer] += checkPoints(sum1, sum2, -1, myDeck, myTable)
            currentPlayer += 1
    return False

def letsPlaySomeCards(playStyle, bonusPoints, ai, players):
    #okay now lets see what we've got from the userInput
    #first the difficulty allows us to create the game deck
    myDeck = gameDeck(playStyle)
    os.system("clear")
    #Now lets make our table and our scoreboard
    myTable = gameTable(playStyle)
    scoreBoard = [0 for i in range(y)]
    #and now we can start the game
    gaming = True
    while gaming:
        gaming = gameON(playStyle, bonusPoints, ai, players, myDeck, myTable)
    print("No potential points to be scored...\n GAME OVER!")
    time.sleep(2)
    os.system("clear")
    print("That was fun! Another round maybe?")
#########################################################################
#########################################################################
'''
The very next thing is a User Interface...
Simple might it seems, its also easy to use for everyone
and quick to debug. We use functions to split the code segments
making our script easy to understand...
We will try to copy this sample
1 play
2 settings
3 learn your decks
4 exit
'''
#########################################################################
######################## U I  C R E A T I O N ###########################
#lets declare our user potential inputs
userInput = 0
playStyle = 0
userSetting = 0
deckPrint = 0
players = 1
tempAnswer = 'n'
#lets declare our settings
bonusPoints = 0
ai = 0
os.system("clear")
print("Hello and welcome to this new trend... Please select mode!")
while int(userInput) != 4:
    print("1 play")
    print("2 settings")
    print("3 learn your decks")
    print("4 exit")
    while True:
      userInput = input("Enter your selection... ")
      if int(userInput) > 0 and int(userInput) < 5:
          break
    if int(userInput) == 1:
        print("Please select a difficulty option...")
        print("1.Easy: Begginer level deck (Max 2 players)")
        print("2.Normal: Okay to play for practise (Max 3 players)")
        print("3.Hard: How the game is meant to be played. Uses all the deck!(Max 4 players)")
        while True:
            playStyle = input("Enter your selection... ")
            if int(playStyle) > 0 and int(playStyle) < 4:
                break
        while True:
            players = input("Enter number of players... Take notice of the selected difficulty and settings!")
            if ai == 1 and int(players) == 1:
                break
            elif int(playStyle) == 1 and int(players) < 3 and int(players) > 0:
                break
            elif int(playStyle) == 2 and int(players) < 4 and int(players) > 0:
                break
            elif int(playStyle) == 3 and int(players) < 5 and int(players) > 0:
                break
        letsPlaySomeCards(int(playStyle), bonusPoints, ai, int(players))
    elif int(userInput) == 2:
        userInput = 0
        print("Please select a setting option to modify...")
        print("1.bonus bonus points on similar suit")
        print("2.ai oppoment (one player only)")
        while True:
          userSetting = input("Enter your selection... ")
          if int(userSetting) > 0 and int(userSetting) < 4:
              break
        while True:
          tempAnswer = input("Are you sure you want to enable this option? y/n")
          if tempAnswer == 'y' or  tempAnswer == 'n':
              break
        if tempAnswer == 'y':
            if userSetting == 1:
                bonusPoints = 1
            else:
                ai = 1
        userSetting = 0
    elif int(userInput) == 3:
        userInput = 0
        print("Please select a difficulty level deck to reveal...")
        print("1.Easy: Begginer level deck")
        print("2.Normal: Okay to play for practise")
        print("3.Hard: How the game is meant to be played. Uses all the deck!")
        while True:
          deckPrint = input("Enter your selection... ")
          if int(deckPrint) > 0 and int(deckPrint) < 4:
              break
        if int(deckPrint) == 1:
            for val, suit in easydeck:
                print('The %s of %s' % (val, suit))
        elif int(deckPrint) == 2:
            for val, suit in normaldeck:
                print('The %s of %s' % (val, suit))
        elif int(deckPrint) == 3:
            for val, suit in deck:
                print('The %s of %s' % (val, suit))
    elif int(userInput) == 4:
        print("We know you'll come back soon <3")
#########################################################################
