import euler54


royal_flush = [[14, 1],
               [13, 1],
               [12, 1],
               [11, 1],
               [10, 1]]

straight_flush = [[13, 1],
                  [12, 1],
                  [11, 1],
                  [10, 1],
                  [9, 1]]

four_of_a_kind = [[1, 1],
                  [1, 2],
                  [1, 3],
                  [1, 4],
                  [2, 1]]

full_house = [[1, 1],
              [1, 2],
              [1, 3],
              [2, 4],
              [2, 1]]

flush = [[2, 1],
         [13, 1],
         [12, 1],
         [11, 1],
         [10, 1]]

straight = [[14, 1],
            [13, 2],
            [12, 3],
            [11, 4],
            [10, 1]]

three_of_a_kind = [[1, 1],
                   [1, 2],
                   [1, 3],
                   [3, 4],
                   [2, 1]]

two_pair = [[5, 1],
            [1, 2],
            [1, 3],
            [2, 4],
            [2, 1]]

pair = [[1, 1],
        [1, 2],
        [4, 3],
        [5, 4],
        [2, 1]]

high_card = [[10, 1],
             [6, 2],
             [8, 3],
             [4, 4],
             [2, 1]]


def test_cardValueStringToNumber():
    assert euler54.cardValueStringToNumbers([[['T', 1], ['J', 1], ['Q', 1]],
                                             [['K', 1], ['A', 1], ['8', 1]]]) == [[[10, 1], [11, 1], [12, 1]],
                                                                                  [[13, 1], [14, 1], [8, 1]]]


def test_cardSuitStringToNumbers():
    assert euler54.cardSuitStringToNumbers([[[1, 'S'], [1, 'C']],
                                            [[1, 'H'], [1, 'D']]]) == [[[1, 1], [1, 2]],
                                                                       [[1, 3], [1, 4]]]


def test_Hand_suits():
    assert euler54.Hand([[1, 1],
                         [1, 2],
                         [1, 3],
                         [1, 4],
                         [2, 1]]).suits() == [1, 2, 3, 4, 1]


def test_Hand_values():
    assert euler54.Hand([[1, 1],
                         [1, 2],
                         [1, 3],
                         [1, 4],
                         [2, 1]]).values() == [1, 1, 1, 1, 2]


def test_Hand_numberOfPairsDict():
    assert euler54.Hand([[1, 1],
                         [1, 2],
                         [2, 2],
                         [3, 2],
                         [4, 2]]).numberOfPairsDict() == dict({1: 2, 2: 1, 3: 1, 4: 1})

    assert euler54.Hand([[1, 1],
                         [1, 2],
                         [1, 3],
                         [3, 2],
                         [4, 2]]).numberOfPairsDict() == dict({1: 3, 3: 1, 4: 1})

    assert euler54.Hand([[1, 1],
                         [1, 2],
                         [1, 3],
                         [1, 4],
                         [4, 2]]).numberOfPairsDict() == dict({1: 4, 4: 1})


def test_Hand_numberOfSuitsDict():
    assert euler54.Hand([[1, 1],
                         [2, 1],
                         [3, 1],
                         [4, 1],
                         [5, 2]]).numberOfSuitsDict() == dict({1: 4, 2: 1})

    assert euler54.Hand([[1, 1],
                         [2, 1],
                         [3, 1],
                         [4, 3],
                         [5, 2]]).numberOfSuitsDict() == dict({1: 3, 3: 1, 2: 1, })

    assert euler54.Hand([[1, 1],
                         [2, 1],
                         [3, 2],
                         [4, 3],
                         [5, 4]]).numberOfSuitsDict() == dict({1: 2, 2: 1, 3: 1, 4: 1})


def test_Hand_isFlush():
    # allowed to be true, because isFlush used to evaluate isRoyalFlush, and isStraightFlush
    # and isRoyalFlush and isStraightFlush will come before isFlush
    assert euler54.Hand(royal_flush).isFlush()
    assert euler54.Hand(straight_flush).isFlush()
    assert euler54.Hand(four_of_a_kind).isFlush() == False
    assert euler54.Hand(full_house).isFlush() == False
    assert euler54.Hand(flush).isFlush()
    assert euler54.Hand(straight).isFlush() == False
    assert euler54.Hand(three_of_a_kind).isFlush() == False
    assert euler54.Hand(two_pair).isFlush() == False
    assert euler54.Hand(pair).isFlush() == False
    assert euler54.Hand(high_card).isFlush() == False


def test_Hand_isStraight():
    # allowed to be true, because isStraght used to evaluate isRoyalFlush, and isStraightFlush
    # and isRoyalFlushand isStraightFlush  will come before isStraight
    assert euler54.Hand(royal_flush).isStraight()
    assert euler54.Hand(straight_flush).isStraight()
    assert euler54.Hand(four_of_a_kind).isStraight() == False
    assert euler54.Hand(full_house).isStraight() == False
    assert euler54.Hand(flush).isStraight() == False
    assert euler54.Hand(straight).isStraight()
    assert euler54.Hand(three_of_a_kind).isStraight() == False
    assert euler54.Hand(two_pair).isStraight() == False
    assert euler54.Hand(pair).isStraight() == False
    assert euler54.Hand(high_card).isStraight() == False


def test_Hand_isRoyalFlush():
    assert euler54.Hand(royal_flush).isRoyalFlush()
    assert euler54.Hand(straight_flush).isRoyalFlush() == False
    assert euler54.Hand(four_of_a_kind).isRoyalFlush() == False
    assert euler54.Hand(full_house).isRoyalFlush() == False
    assert euler54.Hand(flush).isRoyalFlush() == False
    assert euler54.Hand(straight).isRoyalFlush() == False
    assert euler54.Hand(three_of_a_kind).isRoyalFlush() == False
    assert euler54.Hand(two_pair).isRoyalFlush() ==False
    assert euler54.Hand(pair).isRoyalFlush() ==False
    assert euler54.Hand(high_card).isRoyalFlush() ==False



def test_Hand_isStraightFlush():
    assert euler54.Hand(royal_flush).isStraightFlush()
    assert euler54.Hand(straight_flush).isStraightFlush()
    assert euler54.Hand(four_of_a_kind).isStraightFlush() == False
    assert euler54.Hand(full_house).isStraightFlush() == False
    assert euler54.Hand(flush).isStraightFlush() == False
    assert euler54.Hand(straight).isStraightFlush() == False
    assert euler54.Hand(two_pair).isStraightFlush() == False
    assert euler54.Hand(pair).isStraightFlush() == False
    assert euler54.Hand(high_card).isStraightFlush() == False
    assert euler54.Hand(three_of_a_kind).isStraightFlush() == False

def test_Hand_isFourOfAKind():
    assert euler54.Hand(royal_flush).isFourOfAKind() == False
    assert euler54.Hand(straight_flush).isFourOfAKind() == False
    assert euler54.Hand(four_of_a_kind).isFourOfAKind()
    assert euler54.Hand(full_house).isFourOfAKind() == False
    assert euler54.Hand(flush).isFourOfAKind() == False
    assert euler54.Hand(straight).isFourOfAKind() == False
    assert euler54.Hand(two_pair).isFourOfAKind() == False
    assert euler54.Hand(pair).isFourOfAKind() == False
    assert euler54.Hand(high_card).isFourOfAKind() == False
    assert euler54.Hand(three_of_a_kind).isFourOfAKind() == False



def test_Hand_isThreeOfAKind():
    assert euler54.Hand(royal_flush).isThreeOfAKind() == False
    assert euler54.Hand(straight_flush).isThreeOfAKind() == False
    assert euler54.Hand(four_of_a_kind).isThreeOfAKind() == False
    assert euler54.Hand(full_house).isThreeOfAKind() == False
    assert euler54.Hand(flush).isThreeOfAKind() == False
    assert euler54.Hand(straight).isThreeOfAKind() == False
    assert euler54.Hand(two_pair).isThreeOfAKind() == False
    assert euler54.Hand(pair).isThreeOfAKind() == False
    assert euler54.Hand(high_card).isThreeOfAKind() == False
    assert euler54.Hand(three_of_a_kind).isThreeOfAKind()




def test_Hand_isPair():
    assert euler54.Hand(royal_flush).isPair() == False
    assert euler54.Hand(straight_flush).isPair() == False
    assert euler54.Hand(four_of_a_kind).isPair() == False
    assert euler54.Hand(full_house).isPair() == False
    assert euler54.Hand(flush).isPair() == False
    assert euler54.Hand(straight).isPair() == False
    assert euler54.Hand(two_pair).isPair() == False
    assert euler54.Hand(pair).isPair()
    assert euler54.Hand(high_card).isPair() == False
    assert euler54.Hand(three_of_a_kind).isPair() == False



def test_Hand_isTwoPair():
    assert euler54.Hand(royal_flush).isTwoPair() == False
    assert euler54.Hand(straight_flush).isTwoPair() == False
    assert euler54.Hand(four_of_a_kind).isTwoPair() == False
    assert euler54.Hand(full_house).isTwoPair() == False
    assert euler54.Hand(flush).isTwoPair() == False
    assert euler54.Hand(straight).isTwoPair() == False
    assert euler54.Hand(two_pair).isTwoPair()
    assert euler54.Hand(pair).isTwoPair() == False
    assert euler54.Hand(high_card).isTwoPair() == False
    assert euler54.Hand(three_of_a_kind).isTwoPair() == False



def test_Hand_isFullHouse():
    assert euler54.Hand(royal_flush).isFullHouse() == False
    assert euler54.Hand(straight_flush).isFullHouse() == False
    assert euler54.Hand(four_of_a_kind).isFullHouse() == False
    assert euler54.Hand(full_house).isFullHouse()
    assert euler54.Hand(flush).isFullHouse() == False
    assert euler54.Hand(straight).isFullHouse() == False
    assert euler54.Hand(two_pair).isFullHouse() == False
    assert euler54.Hand(pair).isFullHouse() == False
    assert euler54.Hand(high_card).isFullHouse() == False
    assert euler54.Hand(three_of_a_kind).isFullHouse() == False

def test_Hand_weight():
    assert euler54.Hand(royal_flush).weight() == 9
    assert euler54.Hand(straight_flush).weight() == 8
    assert euler54.Hand(four_of_a_kind).weight() == 7
    assert euler54.Hand(full_house).weight() == 6
    assert euler54.Hand(flush).weight() == 5
    assert euler54.Hand(straight).weight() == 4
    assert euler54.Hand(two_pair).weight() == 2
    assert euler54.Hand(pair).weight() == 1
    assert euler54.Hand(high_card).weight() == 0
    assert euler54.Hand(three_of_a_kind).weight() == 3

def test_Hand_subWeight():
    # work in progress
    assert euler54.Hand(royal_flush).subWeight() == [0]
    assert euler54.Hand(straight_flush).subWeight() == [13]
    assert euler54.Hand(four_of_a_kind).subWeight() == [1,2]
    assert euler54.Hand(full_house).subWeight() == [2,1]
    assert euler54.Hand(flush).subWeight() == [13,12,11,10,2]
    assert euler54.Hand(straight).subWeight() == [14]
    assert euler54.Hand(two_pair).subWeight() == [5]
    assert euler54.Hand(pair).subWeight() == [5,4,2]
    assert euler54.Hand(high_card).subWeight() == [10,8,6,4,2]
    assert euler54.Hand(three_of_a_kind).subWeight() == [3,2]

def test_Hand_subWeightHandler():
    assert euler54.Hand(pair).subWeightHandler() == [5,4,2]
    assert euler54.Hand(two_pair).subWeightHandler() == [5]
    assert euler54.Hand(three_of_a_kind).subWeightHandler() == [3,2]
    assert euler54.Hand(four_of_a_kind).subWeightHandler() == [1,2]

def test_Hand_fourOfAKindSubWeight():
    assert euler54.Hand(four_of_a_kind).fourOfAKindSubweight() == [1,2]

def test_Hand_sortedExtraHighCards():
    assert euler54.Hand(high_card).sortedExtraHighCards() == [10,8, 6,4,2]
    assert euler54.Hand(pair).sortedExtraHighCards() == [5,4,2]
    assert euler54.Hand(two_pair).sortedExtraHighCards() == [5]
    assert euler54.Hand(three_of_a_kind).sortedExtraHighCards() == [3,2]

def test_tiebreaker():
    assert euler54.tiebreaker([9,8,7],[8,7,6]) == 1
    assert euler54.tiebreaker([8,7,6],[9,8,7]) == 0

# def test_printWins():
#     assert euler54.printWins(euler54.firstPlayerWeightedHands,
#                             euler54.secondPlayerWeightedHands) ==376