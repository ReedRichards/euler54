import euler54


def test_cardValueStringToNumber():
    assert euler54.cardValueStringToNumbers([[['T', 1], ['J', 1], ['Q', 1]],
                                             [['K', 1], ['A', 1], ['8', 1 ]]]) == [[[10, 1], [11, 1], [12, 1]],
                                                                                  [[13, 1], [14, 1], [8, 1]]]

def test_cardSuitStringToNumbers():
    assert  euler54.cardSuitStringToNumbers([[[1,'S'],[1,'C']],
                                             [[1,'H'],[1,'D']]]) == [[[1,1],[1,2]],
                                                                      [[1,3],[1,4]]]

def test_Hand_suits():
    assert euler54.Hand([[1,1],
                         [1,2],
                         [1,3],
                         [1,4],
                         [2,1]]).suits() == [1,2,3,4,1]

def test_Hand_values():
    assert euler54.Hand([[1,1],
                         [1,2],
                         [1,3],
                         [1,4],
                         [2,1]]).values() == [1,1,1,1,2]

def test_Hand_numberOfPairsDict():
    assert euler54.Hand([[1,1],
                         [1,2],
                         [2,2],
                         [3,2],
                         [4,2]]).numberOfPairsDict() == dict({1: 2, 2: 1, 3: 1, 4: 1})

    assert euler54.Hand([[1,1],
                         [1,2],
                         [1,3],
                         [3,2],
                         [4,2]]).numberOfPairsDict() == dict({1: 3, 3: 1, 4: 1})

    assert euler54.Hand([[1,1],
                         [1,2],
                         [1,3],
                         [1,4],
                         [4,2]]).numberOfPairsDict() == dict({1: 4, 4: 1})

def test_Hand_numberOfSuitsDict():
    assert euler54.Hand([[1,1],
                         [2,1],
                         [3,1],
                         [4,1],
                         [5,2]]).numberOfSuitsDict() == dict({1:4,2:1})

    assert euler54.Hand([[1,1],
                         [2,1],
                         [3,1],
                         [4,3],
                         [5,2]]).numberOfSuitsDict() == dict({1:3,3:1,2:1,})

    assert euler54.Hand([[1,1],
                         [2,1],
                         [3,2],
                         [4,3],
                         [5,4]]).numberOfSuitsDict() == dict({1:2,2:1,3:1,4:1})

def test_Hand_isFlush():
    assert euler54.Hand([[1,1],
                         [2,1],
                         [3,1],
                         [4,1],
                         [5,1]]).isFlush() == True

    assert euler54.Hand([[1,2],
                         [2,1],
                         [3,1],
                         [4,1],
                         [5,1]]).isFlush() == False

def test_Hand_isStraight():
    assert euler54.Hand([[1,1],
                         [2,2],
                         [3,1],
                         [4,2],
                         [5,1]]).isStraight() == True

    assert euler54.Hand([[2,1],
                         [2,2],
                         [3,1],
                         [4,2],
                         [5,1]]).isStraight() == False


