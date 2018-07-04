from hand import Hand

def cardValueStringToNumbers(cardedHandsList):
    # takes a list of hands, with a list of [value,suit] cards
    # returns a list of hands with the values represented as numbers instead of strings
    valuedHand = []
    for hand in cardedHandsList:
        valuedCards = []
        for card in hand:
            if card[0] == 'T':
                card[0] = 10
            if card[0] == 'J':
                card[0] = 11
            if card[0] == 'Q':
                card[0] = 12
            if card[0] == 'K':
                card[0] = 13
            if card[0] == 'A':
                card[0] = 14
            card[0] = int(card[0])
            valuedCards.append(card)
        valuedHand.append(valuedCards)
    return valuedHand


def cardSuitStringToNumbers(cardedHandsList):
    # takes a list of hands, with a list of [value,suit] cards
    # returns a list of hands with the suits represented as numbers instead of strings
    # spades =1
    # clubs = 2
    # hearts = 3
    # diamonds = 4
    valuedHand = []
    for hand in cardedHandsList:
        valuedCards = []
        for card in hand:
            if card[1] == 'S':
                card[1] = 1
            if card[1] == 'C':
                card[1] = 2
            if card[1] == 'H':
                card[1] = 3
            if card[1] == 'D':
                card[1] = 4
            card[1] = int(card[1])
            valuedCards.append(card)
        valuedHand.append(valuedCards)
    return valuedHand


#  get data
with open('poker.txt') as file:
    games = file.read()

# get hands from data
hands = games = games.split('\n')

# convert list of strings to list of lists
handsList = [hand.split() for hand in hands]

# i'd rather compare numbers for values than strings, especially when it comes to a game, so lets convert T,J,Q,K,A to
# 10, 11, 12, 13, 14 and the suits to 1,2,3,4. this will definitely make comparision easier in the future.

# convert hands into a list of value,suit pairs
cardedHandsList = []
for hand in handsList:
    cardList = []
    for card in hand:
        cardList.append(list(card))
    cardedHandsList.append(cardList)

# convert card value,suit pairs into numbers
valuedHand = cardValueStringToNumbers(cardedHandsList)
valuedHand = cardSuitStringToNumbers(valuedHand)

# now that our data is split up and ready for comparison, lets divide the hands into player 1 and player 2
# get player 1 and player 2 hands
firstPlayerHandsList = [hand[0:5] for hand in valuedHand]
secondPlayerHandList = [hand[5:] for hand in valuedHand]


# the initial data pre processing phase is done, lets change each players hands into a value that determines the
# strength of their hand. we will represent this with an array that signifies
# [
#     hand weight (eg. Royal Flush is 10, and a pair is 1)],
#     sub hand weight (pair of aces beats pair of 2's),
# ]
#


# create an arry for each player that is [weight.subweight]
firstPlayerWeightedHands = [[Hand(hand).weight(), Hand(hand).subWeight()] for hand in firstPlayerHandsList]
secondPlayerWeightedHands = [[Hand(hand).weight(), Hand(hand).subWeight()] for hand in secondPlayerHandList]



# breks ties on subweight
def tiebreaker(h1,h2):
    for (tiebreaker1, tiebreaker2) in zip(h1, h2):
        if tiebreaker1 > tiebreaker2:
            return 1
        if tiebreaker2 > tiebreaker1:
            return 0


# evaluates wight and subweight
# returns wins
def wins(p1,p2):
    wins = 0
    for (hand1, hand2) in zip(p1,p2):
        if hand1[0] > hand2[0]:
            wins += 1
            continue
        if hand1[0] == hand2[0]:
            wins += tiebreaker(hand1[1],hand2[1])
    return (wins)



print("Wins: ", wins(firstPlayerWeightedHands,secondPlayerWeightedHands))
