import random
import time
import os
#from kasino import money
money = 100

faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
faceValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
suits = ["♥", "♦", "♣", "♠"]

#initialize variables
help = "Welcome to Kaminski's Blakjak! Here is a list of commands! \n'hit': take a card"

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.name = str(face) + str(suit)
        self.faceValue = 0

    def __str__(self):
        return self.name

class Deck:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)
        return self

    def __str__(self):
        finalString = ""
        for i in range(len(self.cards)):
            finalString += str(self.cards[i])
            finalString += ", "
        return finalString[0:len(finalString)-2]

    def shuffleDeck(self):
        random.shuffle(self.cards)

class Hand(Deck):
    def __init__(self):
        super().__init__()
        self.handValue = 0

    def updateHandValue(self):
        sum = 0
        for i in range(len(self.cards)):
            sum += self.cards[i].faceValue
        aces = 0
        for i in range(len(self.cards)):
            if self.cards[i].face == "A":
                aces += 1
        if aces > 0 and self.handValue > 21:
            sum -= 10
        self.handValue = sum
        return self.handValue

playDeck = Deck()
dealerHand = Hand()
playerHand = Hand()

def createCard(face, suit):
    newCard = Card(face, suit)
    return newCard

def createNormalDeck():
    newDeck = Deck()
    global faces
    global suits
    for i in range(len(suits)):
        for j in range(len(faces)):
            newCard = Card(faces[j], suits[i])
            newCard.faceValue = faceValues[j]
            newDeck.addCard(newCard)
    return newDeck

def createDecks(num):
    newDeck = Deck()
    global faces
    global suits
    for i in range(0,num):
        for i in range(len(suits)):
            for j in range(len(faces)):
                newCard = Card(faces[j], suits[i])
                newCard.faceValue = faceValues[j]
                newDeck.addCard(newCard)
    return newDeck

def dealHand(deck, hand, num):
    for i in range(num):
        temp = deck.cards.pop(0)
        hand.cards.append(temp)
    return hand


#GAME METHODS

def newRound():
    print("\n\n\n")
    global playDeck
    global dealerHand
    global playerHand
    dealerHand = Hand()
    playerHand = Hand()
    dealHand(playDeck, dealerHand, 1)
    dealHand(playDeck, playerHand, 2)
    updateRound()
    if playerHand.handValue == 21 and (dealerHand.handValue != 10 or dealerHand.handValue != 11):
        print("You win! Blackjack!")
        newRound()

def updateRound():
    global dealerHand
    global playerHand
    dealerHand.updateHandValue()
    playerHand.updateHandValue()
    print("Dealer's Hand: " + str(dealerHand))
    print("Dealer's Hand Value: " + str(dealerHand.handValue) + "\n")
    print("Player's Hand: " + str(playerHand))
    print("Player's Hand Value: " + str(playerHand.handValue) + "\n")

def hitt(hand, deck):
     temp = deck.cards.pop(0)
     hand.cards.append(temp)
     hand.updateHandValue()
     updateRound()
     time.sleep(1)

def hitPlayer():
    hitt(playerHand, playDeck)
    if playerHand.handValue > 21:
        print("Player Bust! You lost!")
        newRound()

def dealerGo():
    dealerHand.updateHandValue()
    while dealerHand.handValue < 17:
        hitt(dealerHand, playDeck)
        dealerHand.updateHandValue()

    if dealerHand.handValue > 21:
        print("Dealer Bust! You win this round!")
    elif dealerHand.handValue > playerHand.handValue:
        print("Dealer wins.")
    elif dealerHand.handValue == playerHand.handValue:
        print("Push.")
    else:
        print("You win!")

    time.sleep(1)
    newRound()


def commands(inputText):
    global playerHand
    global playDeck
    switcher = {
        "play": newRound,
        "stay": dealerGo,
        "hit": hitPlayer,
        #"end": endGame
    }
    func = switcher.get(inputText, lambda: "Try again.")
    return func()

def initBlackjack():
    global playDeck
    playDeck = createDecks(6)
    playDeck.shuffleDeck()
    newRound()

def blackjackConsole():
    global money
    print("")
    if money <= 0:
        print("Your game is over, you lost all your money! Thanks for playing!")
    else:
        userSaysUpper = input("What would you like to do? ")
        userSays = userSaysUpper.lower()
        commands(userSays)
        blackjackConsole()

#def endGame():
 #   print("Thanks for playing!")
  #  exit()
   # os.system('python kasino.py')


print(help)
initBlackjack()
blackjackConsole()




#mainDeck = Deck()
#mainDeck.addCard(Card("Nine", "Diamonds"))
#mainDeck.addCard(Card("Ten", "Diamonds"))
#print(mainDeck)
#normalDeck = createNormalDeck()
#print(normalDeck)
#createCard("Five", "Spades")

initBlackjack()