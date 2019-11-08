from functionaltools import tail



def test_tail_list():
    assert tail([1,2,3,4]) == [2,3,4]


def test_tail_string():
    assert tail("abcdefg") == "bcdefg"