import random
import time
#from kasino import money
money = 100

comeOut = True
point = None
rollValue = 1
bet = 5
keepGoing = True
comePrep = False
comeList = []
tempList = []

help = "Welcome to Kaminski's Kraps! Here is a list of commands! \nenter key - roll once\n'play' - play through a point cycle (not recommended)\n come - set a come bet for the next roll \n'end' or 'stop' - end the program \n'bet' - change bet(s) \n'help' - display this help message again"

def rollOneDie():
    return random.randint(1, 6);

def rollDice(num):
    global rollValue
    dieSum = 0
    for i in range(0, num):
        dice = rollOneDie()
        print("       " + str(dice))
        dieSum += dice
    print("Sum:   " + str(dieSum))
    rollValue = dieSum

def rollCraps():
    rollDice(2)
    global comeOut
    global rollValue
    global point
    global money
    global keepGoing
    global comePrep
    global tempList
    global comeList
    global bet
    global tableChips
    global comeChips
    print("Point: " + str(point))
    if comeOut == True:
        print("Coming out!")
        if rollValue == 7 or rollValue == 11:
            money += bet
            print("You won $" + str(bet) + " on a come-out roll!")
            keepGoing = False
            point = None
            if rollValue == 7:
                if len(comeList) > 0 or comePrep == True:
                    print("All come bets have been removed. You lost $" + str(comeChips) + ". ")
                    comeList = []

        elif rollValue == 2 or rollValue == 3 or rollValue == 12:
            money -= bet
            print("Craps! You lost $" + str(bet) + " on a come-out roll!")
            keepGoing = False
            point = None
        else:
            point = rollValue
            print("Point set to " + str(point) + ".")
            keepGoing = True
            comeOut = False
    else:
        if point == rollValue:
            money += bet
            comeOut = True
            print("Point made! You won $" + str(bet) + "! The next roll is a come-out.")
            checkCome()
            comeAdd()
            tempList = []
            keepGoing = False
            point = None
        elif rollValue == 7:
            comeOut = True
            money -= bet
            print("Seven-out. You lost $" + str(tableChips) + " in total! The next roll is a come-out.")
            if len(comeList) > 0 or comePrep == True:
                print("All come bets have been removed.")
                comeList = []
            keepGoing = False
            point = None
            tempList = []
        else:
            comeOut = False
            print("Roll again!")
            keepGoing = True
            #COME STUFF
            if (rollValue == 2 or rollValue == 3 or rollValue == 12) and comePrep == True:
                print("Craps! Can't add come bet, you lost it, but odds come back")
                money += tempList[1]
                tempList = []
            elif rollValue == 11 and comePrep == True:
                print("YO! Can't add come bet, you won even money and odds come back")
                money += (tempList[0] * 2)
                money += tempList[1]
                tempList = []
            else:
                checkCome()
                comeAdd()

    comePrep = False

    print("")
    print("Chip Total in Bank: $" + str(money))
    allChips = money
    allChips += bet
    for i in comeList:
        allChips += i[0]
        allChips += i[1]
    tableChips = allChips - money
    comeChips = 0
    for i in comeList:
        comeChips += i[0]
        comeChips += i[1]
    print("Chip Total in Bank + Table: $" + str(allChips) + "\n")
    print("Bets:")
    print("Pass Line Bet: $" + str(bet))
    print
    comeNums = ""
    for i in comeList:
        comeNums += "come bet on " + str(i[2]) + " for $" + str(i[0]) + " and odds of " + str(i[1]) +". "
    print("Come Bets: " + comeNums)
    for i in range(3):
        print("")

def playCraps():
    global comeOut
    global keepGoing
    time.sleep(2)
    rollCraps()
    if keepGoing == True:
        playCraps()
    else:
        print("End of point cycle.")
        time.sleep(2)
        crapsConsole()

def playy():
    playCraps()

def endOrStop():
    print("Thanks for playing! Your chip total is $" + str(money) + ".")
    exit()
    #os.system('python kasino.py')

def helpp():
    global help
    print(help)
    crapsConsole()

def bett():
    global bet
    global money
    if comeOut == True:
        print("Type value to change bet to.")
        try:
            betTest = int(input("Enter bet value: $"))
        except ValueError:
            print("Value not understood.")
            bett()
        if betTest > money or betTest < 0:
            print("You know your limits.")
            bett()
        else:
            money += bet
            bet = betTest
            print("New bet value set to $" + str(bet) + ".")
            money -= bet
    else:
        print("Can't set pass bet on another roll other than come out")
    crapsConsole()

def addChips():
    global money
    amount = int(input("How much? $"))
    money += amount
    print("chip count now $" + str(money))


    #COME BET STUFF
def comePrepp():
    global comePrep
    global comeList
    global tempList
    global money
    if comeOut == True:
         print("Can't make come bets on come-out roll!")
    else:
        comePrep = True
        try:
            comeBet = int("0" + input("How much for your come bet? $"))
            if comeBet > money or comeBet <= 0:
                print("You know your limits.")
                comePrepp()
        except ValueError:
            print("Value not understood.")
            comePrepp()

        else:
            try:
                comeOdds = int("0" + input("How much for the odds on your come bet? $"))
                if comeOdds > money or comeOdds <= 0:
                    print("You know your limits.")
                    comePrepp()
                else:
                    tempList.append(comeBet)
                    tempList.append(comeOdds)
                    money -= comeBet
                    money -= comeOdds
                    print("Money left: $" + str(money))
            except ValueError:
                print("Value not understood.")
                comePrepp()


def comeAdd():
    global comePrep
    global comeList
    global tempList
    global rollValue
    if comePrep == True:
        print("Come bet moved to " + str(rollValue) + "!")
        tempList.append(rollValue)
        comeList.append(tempList)
        #print(comeList)
        tempList = []
        comePrep = False

def odds(v, b):
    if v == 4 or v == 10:
        return int(b * 2)
    elif v == 5 or v == 9:
        return int(b * 1.5)
    elif v == 6 or v == 8:
        return int(b * 1.167)
    else:
        return int(b)


def checkCome():
    global comePrep
    global comeList
    global tempList
    global rollValue
    global money
    for i in comeList:
        if rollValue == i[2]:
            wins = odds(rollValue, i[1])
            money += i[0] * 2
            money += i[1]
            money += wins
            print("You won $" + str(i[0] + wins) + " from your come bet on " + str(i[2]) + ". \nYour initial bet of $" + str(i[0]) + " and odds of $" + str(i[1]) + " has also been returned to your money pile.")
            comeList.remove(i)






def commands(inputText):
    switcher = {
        "play": playy,
        "\r": playy,
        "": rollCraps,
        "end": endOrStop,
        "stop": endOrStop,
        "help": helpp,
        "bet": bett,
        "come": comePrepp,
        "addchips": addChips
    }
    func = switcher.get(inputText, lambda: "Try again.")
    return func()

def crapsConsole():
    global money
    print("")
    if money <= 0:
        print("Your game is over, you lost all your money! Thanks for playing!")
    else:
        userSaysUpper = input("Craps Command: ")
        userSays = userSaysUpper.lower()
        commands(userSays)
        crapsConsole()

print(help)
money -= bet
crapsConsole()

#for tomorrow: come bets are done in an array of subarrays with number to roll and price bet.
#make a line in console that shows all bets on the table (pass line is default), this is another array