from collections import Counter


def cardValueStringToNumbers(cardedHandsList):
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
#     and remaing values being high cards sorted highest to lowest for tie breakers
# ]
#
# so according to this a royal flush would be represented as [10] because it is the highest possible hand, and will not
# require additional parameters, and a pair of 3's with Ace, King, Queen, would be represented as [1,14,13,12]
#
# this could also be done with class Hand with methods weight, subweight, and tiebreaker, but I feel like the above will
# be simpler to evaluate despite the classes being easier to encode, but in real life I'd probably do both, and see
# which is more efficient.

# the first theing we are going to check for is whether or not the hand is a royal flush, so we need to make
# two functions, isFlush(), and isSequence() those functions will also be calling getSuits() and getValues() so we will

class Hand:
    # takes an hand array containing integers of [value,suit] and operates on them
    # Hand([[1,1],
    #       [1,2],
    #       [1,3],
    #       [1,4],
    #       [2,1]]).suits() => [1,2,3,4,1]

    def __init__(self, hand):
        self.hand = hand

    def suits(self):
        # returns an array containing suits
        # Hand([[1,1],[1,2],[1,3],[1,4],[2,1]]).suits() => [1,2,3,4,1]
        suits = []
        for card in self.hand:
            suits.append(card[1])
        return suits

    def values(self):
        # returns an array containing values
        # Hand([[1, 1], [1, 2], [1, 3], [1, 4], [2, 1]]).values() => [1, 1, 1, 1, 2]
        values = []
        for card in self.hand:
            values.append(card[0])
        return values

    def numberOfPairsDict(self):
        # should rename to numberOfValueOccurrences
        # returns a dictionary with number of occurrences of each value
        # Hand([[1,1],
        #       [1,2],
        #       [2,2],
        #       [3,2],
        #       [4,2]]).numberOfPairsDict() => dict({1: 2, 2: 1, 3: 1, 4: 1})
        values = self.values()
        return dict(Counter(values))

    def numberOfSuitsDict(self):
        # should rename to numberOfSuitOccurrences
        # returns a dictionary with number of occurrences of each value
        # Hand([[1,1],
        #       [1,2],
        #       [2,2],
        #       [3,2],
        #       [4,2]]).numberOfPairsDict() => dict({1: 1, 2: 4})
        suits = self.suits()
        return dict(Counter(suits))

    def isFlush(self):
        # returns true if hand is flush, false if hand is not flush
        # Hand([[1,1],
        #       [2,1],
        #       [3,1],
        #       [4,1],
        #       [5,1]]).isFlush() => True
        suitsDict = self.numberOfSuitsDict()
        for key, value in suitsDict.items():
            if value == 5:
                return True
        return False

    def isStraight(self):
        # refactor
        # returns true if values are consecutive
        values = self.values()
        hv = max(values)
        if hv - 1 in values:
            if hv - 2 in values:
                if hv - 3 in values:
                    if hv - 4 in values:
                        return True
        return False

    def isRoyalFlush(self):
        # returns True if hand is royal flush
        is_straight = self.isStraight()
        is_flush = self.isFlush()
        values = self.values()
        maximum = max(values)
        return is_flush and is_straight and maximum == 14

    def isStraightFlush(self):
        # if hand is straight and flush returns true
        # returns false otherwise
        is_straight = self.isStraight()
        is_flush = self.isFlush()
        return is_straight and is_flush

    def isFourOfAKind(self):
        # returns true if there are four matching values,
        # returns false if there are not for matching values
        pairs = self.numberOfPairsDict()
        for key, value in pairs.items():
            if value == 4:
                return True
        return False

    def isThreeOfAKind(self):
        pairs = self.numberOfPairsDict()
        iter = 0
        for key, value in pairs.items():
            if value == 3:
                iter += 1
            if value == 2:
                iter -= 1
        return iter == 1

    def isPair(self):
        pairs = self.numberOfPairsDict()
        iter = 0
        for key, value in pairs.items():
            if value == 2:
                iter += 1
            if value == 3:
                iter -= 1
        return iter == 1

    def isTwoPair(self):
        pairs = self.numberOfPairsDict()
        iter = 0
        for key, value in pairs.items():
            if value == 2:
                iter += 1
        return iter == 2

    def isFullHouse(self):
        pairs = self.numberOfPairsDict()
        iter = 0
        for key, value in pairs.items():
            if value == 3:
                iter += 1
            if value == 2:
                iter += 2
        return iter == 3



    def weight(self):
        if self.isRoyalFlush():
            return 9
        if self.isStraightFlush():
            return 8
        if self.isFourOfAKind():
            return 7
        if self.isFullHouse():
            return 6
        if self.isFlush():
            return 5
        if self.isStraight():
            return 4
        if self.isThreeOfAKind():
            return 3
        if self.isTwoPair():
            return 2
        if self.isPair():
            return 1
        return 0

    def subWeight(self):
        weight = self.weight()
        values = self.values()
        # royal flush
        if self.isRoyalFlush():
            return [0]
        # straight flush
        if weight == 8:
            # high card beats equal straight flushes
            return [max(values)]
        # four of a kind
        if weight == 7:
            # high card beats a tie
            # sorted for ultimate tiebreaker of final high card
            return self.subWeightHandler()
        # full house
        if weight == 6:
            # high card beats tie, if equal, low card beats tie
            return [max(values), min(values)]
        # flush
        if weight == 5:
            # iterate cards highest to lowest
            return sorted(values, reverse=True)
        # straight
        if weight == 4:
            # high card beats tie
            return [max(values)]
        # three of a kind
        if weight == 3:
            return self.subWeightHandler()
        # two pair
        if weight == 2:
            return self.subWeightHandler()
        # one pair
        if weight == 1:
            return self.subWeightHandler()
        # high card
        if weight == 0:
            return sorted(values, reverse=True)

    def subWeightHandler(self):
        if self.isFourOfAKind():
            return self.fourOfAKindSubweight()
        return self.sortedExtraHighCards()

    def fourOfAKindSubweight(self):
        pairsDict = self.numberOfPairsDict()
        subweight =[0,0]
        for key, value in pairsDict.items():
            if value == 1:
                subweight[1] = key
            if value == 4:
                subweight[0] = key
        return subweight

    def sortedExtraHighCards(self):
        ## this is where I messed up
        pairsDict = self.numberOfPairsDict()
        cards = []
        for key, value in pairsDict.items():
            if value == 1:
                cards.append(key)
        return sorted(cards, reverse=True)

firstPlayerWeightedHands = [[Hand(hand).weight(), Hand(hand).subWeight()] for hand in firstPlayerHandsList]
secondPlayerWeightedHands = [[Hand(hand).weight(), Hand(hand).subWeight()] for hand in secondPlayerHandList]

wins = 0
for (hand1, hand2) in zip(firstPlayerWeightedHands, secondPlayerWeightedHands):
    if hand1[0] > hand2[0]:
        wins += 1
        continue
    if hand1[0] == hand2[0]:
        for (tiebreaker1, tiebreaker2) in zip(hand1[1], hand2[1]):
            if tiebreaker1 > tiebreaker2:
                wins += 1
                break
            if tiebreaker2 > tiebreaker1:
                break

print(wins)
