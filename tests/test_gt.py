from functionaltools import gt


def test_gt():
    over_five = gt(5)
    assert over_five(6) == True
    assert over_five(5) == False
    assert over_five(4) == False