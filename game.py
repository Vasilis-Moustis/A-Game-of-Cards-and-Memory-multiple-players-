#########################################################################
#########################  I M P O R T S ################################
# you gonna need to install sys from pip3

import itertools
import random
import array
import time
import os


#########################################################################
################  A R E  W E  D O N E  P L A Y I N G  ###################
def checkGameProgress(myTable):
    counter = 0
    for value in myTable:
        if value == 'X':
            counter +=1
    if counter < 2 :
        return False
    else:
        return True


def checkSimilarValues(playStyle, bonusPoints, myDeck, myTable):
    k = 0
    if playStyle == 1:
        k = 16
    elif playStyle == 2:
        k = 40
    else:
        k = 52
    for i in range (k):
        if myTable[i] == 'X':
            for j in range (i+1 , k):
                if myDeck[j][0] == myDeck[i][0] and myTable[j] == 'X':
                    return True
    return False

def checkSimilarSymbols(playStyle, bonusPoints, myDeck, myTable):
    k = 0
    if playStyle == 1:
        k = 16
    elif playStyle == 2:
        k = 40
    else:
        k = 52
    for i in range(k):
        if myTable[i] == 'X':
            for j in range (i+1 , k):
                if myDeck[j][1] == myDeck[i][1] and myTable[j] == 'X':
                    return True
    return False

def checkPotentialPoints(playStyle, bonusPoints, myDeck, myTable):
    if playStyle == 1:
        return checkGameProgress(myTable)
    else:
        if bonusPoints:
            return checkSimilarValues(playStyle, bonusPoints, myDeck, myTable) and checkSimilarSymbols(playStyle, bonusPoints, myDeck, myTable)
        else:
            return checkSimilarValues(playStyle, bonusPoints, myDeck, myTable)
#########################################################################

#First things first, we need a deck.
#Like  every programmer, we seek for the easiest way possible
#We sure can do the [[..], [..], ....] thing but this looks wayy cleaner

#########################################################################
################## D E C K   C R E A T I O N ############################

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
worthings = [] #what scores what
myc = 0
for card in Vals2:
    if card == 'A':
        worthings.append([card,1])
        break
    worthings.append([card,scorings[myc]])
    myc +=1

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
def electWinner(scoreBoard):
    counter = 1
    max = 0
    maxi = 0
    draw = False
    drawi = 0
    for score in scoreBoard:
        if score > max:
            max = score
            maxi = counter
            draw = False
        elif score == max:
            draw = True
            drawi = counter
        counter += 1
    if not draw:
        print("The big winner is Player " + str(maxi) + " !\n")
    else:
        print("The game is a draw between Player " + str(maxi) + " and Player " + str(drawi) + " !\n")
    time.sleep(5)


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
                print(mydeck[i*10 +j][0], end="", flush=True)
                print(mydeck[i*10 + j][1], end = "\t", flush=True)
        time.sleep(3)
    elif playStyle == 3:
        mydeck = list(itertools.product(Vals2, symbols))
        random.shuffle(mydeck)
        for i in range (0,4):
            print("\n")
            for j in range (0,13):
                print(mydeck[i*13 +j][0], end="", flush=True)
                print(mydeck[i*13 + j][1], end = "\t", flush=True)
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

def printCurrentOpportunities(playStyle, myTable):
    if playStyle == 1 :
        for i in range (0,4):
            print("\n")
            for j in range (0,4):
                print(myTable[i * 4 + j ], end = "\t", flush=True)
    elif playStyle == 2:
        for i in range (0,4):
            print("\n")
            for j in range (0,10):
                print(myTable[i * 10 + j ], end = "\t", flush=True)
    elif playStyle == 3:
        for i in range (0,4):
            print("\n")
            for j in range (0,13):
                print(myTable[i * 13 + j ], end = "\t", flush=True)
    print("\n")

def printscoreBoard(scoreBoard):
    os.system("clear")
    c = 1
    for player in scoreBoard:
        print("Player " + str(c) + ":  "  + str(player) + " Points")
        c += 1
    print("\n")
    time.sleep(5)

#########################################################################
##################### G A M E  F U N C T I O N S  #######################


def checkKings(s1, s2, myDeck,myTable):
    if myDeck[s1][0] in specials and myDeck[s2][0] in specials:
        if myDeck[s1][0] == 'K' and myDeck[s2][0] == 'K':
            if checkGameProgress(myTable):
                return True
    return False

def checkJacks(s1, s2, myDeck,myTable):
    if myDeck[s1][0] in specials and myDeck[s2][0] in specials:
        if checkGameProgress(myTable):
            if myDeck[s1][0] == 'J' and myDeck[s2][0] == 'J':
                print("You won another round!")
                return True
    return False

def checkThirdDrawPotential(sum1, sum2, myDeck, myTable):
    if myDeck[sum1][0] in specials and myDeck[sum2][0] in specials:
        if checkGameProgress(myTable):
            if myDeck[sum1][0] == 'Q' and myDeck[sum2][0] == 'J':
                print("You won another pick!")
                return True
            elif myDeck[sum1][0] == 'J' and myDeck[sum2][0] == 'Q':
                print("You won another pick!")
                return True
    return False

def flipCards(sum1, sum2, sum3, myDeck, myTable,worth1, worth2, worth3):
    if worth1 == worth2 and worth3 == -1:
        myTable[sum1] = myDeck[sum1][0] + "" + myDeck[sum1][1]
        myTable[sum2] = myDeck[sum2][0] + "" + myDeck[sum2][1]
    elif worth3 != -1:
        if worth1 == worth2 and worth1 == worth3 and worth3 == worth2:
            myTable[sum1] = myDeck[sum1][0] + "" + myDeck[sum1][1]
            myTable[sum2] = myDeck[sum2][0] + "" + myDeck[sum2][1]
            myTable[sum3] = myDeck[sum3][0] + "" + myDeck[sum3][1]
        elif worth1 == worth2:
            myTable[sum1] = myDeck[sum1][0] + "" + myDeck[sum1][1]
            myTable[sum2] = myDeck[sum2][0] + "" + myDeck[sum2][1]
        elif worth1 == worth3:
            myTable[sum1] = myDeck[sum1][0] + "" + myDeck[sum1][1]
            myTable[sum3] = myDeck[sum3][0] + "" + myDeck[sum3][1]
        elif worth2 == worth3:
            myTable[sum2] = myDeck[sum2][0] + "" + myDeck[sum2][1]
            myTable[sum3] = myDeck[sum3][0] + "" + myDeck[sum3][1]

def checkPoints(sum1, sum2, sum3, myDeck, myTable, scoreBoard, currentPlayer, bonusPoints):
    time.sleep(2)
    added1, added2, added3 = False, False, False
    worth1, worth2, worth3 = -1,-1,-1
    symbol1, symbol2 = '' , ''
    score = 0
    for matches in worthings:
        if matches[0] == myDeck[sum1][0] and not added1:
            score += matches[1]
            worth1 = matches[1]
            added1 = True
            symbol1 = myDeck[sum1][1]
        if matches[0] == myDeck[sum2][0] and not added2:
            score += matches[1]
            worth2 = matches[1]
            added2 = True
            symbol2 = myDeck[sum2][1]
        if sum3 != -1 and matches[0] == myDeck[sum3][0] and not added3:
            score += matches[1]
            worth3 = matches[1]
            added3 = True
    flipCards(sum1, sum2, sum3, myDeck, myTable,worth1, worth2, worth3)
    if bonusPoints and symbol1 == symbol2:
        print("\n+10 points for same symbols!\n")
        score += 10
    print("Totally scored " + str(score) + " points on this round!\n")
    scoreBoard[currentPlayer - 1] += score
    time.sleep(4)
    printscoreBoard(scoreBoard)

def gameON(playStyle, bonusPoints, ai, players, myDeck, myTable, scoreBoard):
    currentPlayer = 1
    line, column = -1,-1
    mline, mcolumn = 4,0
    sum1,sum2,sum3 = 0,0,0
    if playStyle == 1 :
        mcolumn  = 4
    elif playStyle == 2:
        mcolumn = 10
    elif playStyle == 3:
        mcolumn = 13
    while checkPotentialPoints(playStyle, bonusPoints, myDeck, myTable):
        os.system("clear")
        printCurrentOpportunities(playStyle, myTable)
        if currentPlayer > players:
            currentPlayer -= players
        while True:
            while True:
              line = input("Player " + str(currentPlayer) + " choose line number\n")
              if int(line) > 0 and int(line) <= mline:
                  break
            while True:
              column = input("Player " + str(currentPlayer) + " choose column number\n")
              if int(column) > 0 and int(column) <= mcolumn:
                  break
            sum1 = int(line) * mcolumn - mcolumn + int(column) -1
            if myTable[sum1] == 'X':
                break
            else:
                print("This card has already been flipped\n")
        print("You draw " + myDeck[sum1][0] + myDeck[sum1][1])
        while True:
            while True:
              line = input("Player " + str(currentPlayer) + " choose line number\n")
              if int(line) > 0 and int(line) <= mline:
                  break
            while True:
              column = input("Player " + str(currentPlayer) + " choose column number\n")
              if int(column) > 0 and int(column) <= mcolumn:
                  break
            sum2 = int(line) * mcolumn - mcolumn + int(column) -1
            if myTable[sum2] == 'X':
                break
            else:
                print("This card has already been flipped\n")
        print("You draw " + myDeck[sum2][0] + myDeck[sum2][1])
        if checkKings(sum1, sum2, myDeck, myTable):
            print("Calculating score for player " + str(currentPlayer) + "...\n")
            if bonusPoints:
                print("Bonus Points for same symbols will be accounted...\n")
            checkPoints(sum1, sum2, -1, myDeck, myTable, scoreBoard, currentPlayer, bonusPoints)
            currentPlayer += 2
        elif checkJacks(sum1, sum2, myDeck, myTable):
            print("Calculating score for player " + str(currentPlayer) + "...\n")
            if bonusPoints:
                print("Bonus Points for same symbols will be accounted...\n")
            checkPoints(sum1, sum2, -1, myDeck, myTable, scoreBoard, currentPlayer, bonusPoints)
        elif checkThirdDrawPotential(sum1, sum2, myDeck, myTable):
            while True:
                while True:
                  line = input("Player " + str(currentPlayer) + " choose line number\n")
                  if int(line) > 0 and int(line) <= mline:
                      break
                while True:
                  column = input("Player " + str(currentPlayer) + " choose column number\n")
                  if int(column) > 0 and int(column) <= mcolumn:
                      break
                sum3 = int(line) * mcolumn - mcolumn + int(column) -1
                if myTable[sum3] == 'X':
                    break
                else:
                    print("This card has already been flipped\n")
            print("You draw " + myDeck[sum3][0] + myDeck[sum3][1])
            print("Calculating score for player " + str(currentPlayer) + "...\n")
            if bonusPoints:
                print("Bonus Points for same symbols will be accounted...\n")
            checkPoints(sum1, sum2, sum3, myDeck, myTable, scoreBoard, currentPlayer, bonusPoints)
            currentPlayer += 1
        else:
            print("Calculating score for player " + str(currentPlayer) + "...\n")
            if bonusPoints:
                print("Bonus Points for same symbols will be accounted...\n")
            checkPoints(sum1, sum2, -1, myDeck, myTable, scoreBoard, currentPlayer, bonusPoints)
            currentPlayer += 1
    return False


def letsPlaySomeCards(playStyle, bonusPoints, ai, players):
    #okay now lets see what we've got from the userInput
    #first the difficulty allows us to create the game deck
    myDeck = gameDeck(playStyle)
    os.system("clear")
    #Now lets make our table and our scoreBoard
    myTable = gameTable(playStyle)
    scoreBoard = [0 for i in range(int(players))]
    #and now we can start the game
    gaming = True
    while gaming:
        gaming = gameON(playStyle, bonusPoints, ai, players, myDeck, myTable, scoreBoard)
    print("No potential points to be scored...\n GAME OVER!\n")
    electWinner(scoreBoard)
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
bonusPoints = False
ai = False
os.system("clear")
print("Hello and welcome to this new trend... Please select mode!")
while int(userInput) != 4:
    print("1 play")
    print("2 settings")
    print("3 learn your decks")
    print("4 exit")
    try:
        while True:
          userInput = input("Enter your selection... ")
          if int(userInput) > 0 and int(userInput) < 5:
              break
    except ValueError as e:
        pass
    if int(userInput) == 1:
        print("Please select a difficulty option...")
        print("1.Easy: Begginer level deck (2 players)")
        print("2.Normal: Okay to play for practise (2-3 players)")
        print("3.Hard: How the game is meant to be played. Uses all the deck!(2-4 players)")
        while True:
            playStyle = input("Enter your selection... ")
            if int(playStyle) > 0 and int(playStyle) < 4:
                break
        while True:
            players = input("Enter number of players... Take notice of the selected difficulty and settings!")
            if ai == 1 and int(players) == 1:
                break
            elif int(playStyle) == 1 and int(players) == 2:
                break
            elif int(playStyle) == 2 and int(players) < 4 and int(players) > 1:
                break
            elif int(playStyle) == 3 and int(players) < 5 and int(players) > 1:
                break
        letsPlaySomeCards(int(playStyle), bonusPoints, ai, int(players))
    elif int(userInput) == 2:
        userInput = 0
        print("Please select a setting option to modify...")
        print("1.bonus bonus points on similar suit")
        print("2.ai oppoment (one player only)")
        try:
            while True:
              userSetting = input("Enter your selection... ")
              if int(userSetting) > 0 and int(userSetting) < 3:
                  break
        except ValueError as e:
            pass
        try:
            while True:
              tempAnswer = input("Are you sure you want to enable this option? y/n")
              if tempAnswer == 'y' or  tempAnswer == 'n':
                  break
        except ValueError as e:
            pass
        if tempAnswer == 'y':
            if int(userSetting) == 1:
                bonusPoints = True
            else:
                ai = True
        userSetting = 0
    elif int(userInput) == 3:
        userInput = 0
        print("Please select a difficulty level deck to reveal...")
        print("1.Easy: Begginer level deck")
        print("2.Normal: Okay to play for practise")
        print("3.Hard: How the game is meant to be played. Uses all the deck!")
        print("4.See whay each card worths!")
        try:
            while True:
              deckPrint = input("Enter your selection... ")
              if int(deckPrint) > 0 and int(deckPrint) < 5:
                  break
        except ValueError as e:
            pass
        if int(deckPrint) == 1:
            for val, suit in easydeck:
                print('The %s of %s' % (val, suit))
        elif int(deckPrint) == 2:
            for val, suit in normaldeck:
                print('The %s of %s' % (val, suit))
        elif int(deckPrint) == 3:
            for val, suit in deck:
                print('The %s of %s' % (val, suit))
        elif int(deckPrint) == 4:
            for val, suit in worthings:
                print('The %s scores %s' % (val, suit))
    elif int(userInput) == 4:
        print("We know you'll come back soon <3")
#########################################################################
