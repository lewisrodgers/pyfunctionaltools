from functionaltools import complement, equals


def test_complement():
    is_zero = equals(0)
    not_zero = complement(is_zero)
    assert not_zero(0) == False
    assert not_zero(1) == True