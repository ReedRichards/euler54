from collections import Counter

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
        # returns true hand is a three of a kind,
        # also makes sure that its not a full houes
        pairs = self.numberOfPairsDict()
        iter = 0
        for key, value in pairs.items():
            if value == 3:
                iter += 1
            if value == 2:
                iter -= 1
        return iter == 1

    def isPair(self):
         # returns true if pair
         # returns false otherwis, also test to make sure its not a
         # full house or two pair
        pairs = self.numberOfPairsDict()
        iter = 0
        for key, value in pairs.items():
            if value == 2:
                iter += 1
            if value == 3:
                iter -= 1
        return iter == 1

    def isTwoPair(self):
        # returns true if two pair
        # also checks to make sure its not a regular pair
        pairs = self.numberOfPairsDict()
        iter = 0
        for key, value in pairs.items():
            if value == 2:
                iter += 1
        return iter == 2

    def isFullHouse(self):
        # returns true if full house
        pairs = self.numberOfPairsDict()
        iter = 0
        for key, value in pairs.items():
            if value == 3:
                iter += 1
            if value == 2:
                iter += 2
        return iter == 3



    def weight(self):
        # returns an integer representing card weight based on hand
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
        # returns a subweight to break ties
        weight = self.weight()
        values = self.values()
        if self.isRoyalFlush():
            return [0]
        if self.isStraightFlush():
            # high card beats equal straight flushes
            return [max(values)]
        if self.isFourOfAKind():
            return self.subWeightHandler()
        if self.isFullHouse():
            return [max(values), min(values)]
        if self.isFlush():
            return sorted(values, reverse=True)
        if self.isStraight():ye
            return [max(values)]
        if self.isThreeOfAKind():
            return self.subWeightHandler()
        if self.isTwoPair():
            return self.subWeightHandler()
        if self.isPair():
            return self.subWeightHandler()
        if weight == 0:
            return sorted(values, reverse=True)

    def subWeightHandler(self):
        if self.isFourOfAKind():
            return self.fourOfAKindSubweight()
        if self.isPair() == 1:
            return self.pairSubWeight()
        return self.sortedExtraHighCards()

    def pairSubWeight(self):
        pairsDict = self.numberOfPairsDict()
        subweight = []
        highCards =[]
        for key, value in pairsDict.items():
            if value == 2:
                subweight.append(key)
            else:
                highCards.append(key)
        highCards.sort(reverse=True)
        for card in highCards:
            subweight.append(card)

        return subweight




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
