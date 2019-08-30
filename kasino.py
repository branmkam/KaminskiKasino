import os
money = 100
print("Welcome to the Kaminski Kasino! Type in what you'd like to play and press enter twice!")
def commands(inputText):
    switcher = {
        "craps": runCraps,
        "blackjack": runBlackjack,
    }
    func = switcher.get(inputText, lambda: "Try again.")
    return func()

def runFile(filename):
    name = "python " + str(filename) + ".py"
    os.system(name)

def runCraps():
    runFile("nodice3")

def runBlackjack():
    runFile("blackjack2")

def kasinoKonsole():
    global money
    print("")
    if money <= 0:
        print("Your time at the casino is over, you lost all your money! Thanks for playing!")
        exit()
    else:
        userSaysUpper = input("What would you like to play? ")
        userSays = userSaysUpper.lower()
        commands(userSays)
        #if userSays != "craps" or userSays != "blackjack":
        kasinoKonsole()

#print(help)
kasinoKonsole()