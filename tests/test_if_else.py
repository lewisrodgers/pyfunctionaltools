from functionaltools import const, equals, identity, if_else


def test_if_else():
    is_jim = if_else(
        equals("jim"),
        const("halpert"),
        identity
    )
    assert is_jim("jim") == "halpert"
    assert is_jim("pam") == "pam"


def test_if_else_multi():
    is_jim = if_else(
        equals("jim"),
        const("hi jim"),
        const("hi other")
    )
    who_is = if_else(
        equals("pam"),
        const("hi pam"),
        is_jim
    )
    assert who_is("jim") == "hi jim"
    assert who_is("pam") == "hi pam"
    assert who_is("other") == "hi other"
