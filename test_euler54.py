import euler54


def test_cardValueStringToNumber():
    assert euler54.cardValueStringToNumbers([['T', 1], ['J', 1], ['Q', 1], ['K', 1], ['A', 1]]) == [[10, 1], [11, 1][12, 1],
                                                                                          [13, 1], [14, 1]]
