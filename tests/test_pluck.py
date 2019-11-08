from functionaltools import pluck


def test_pluck():
    people = [
        {"name": "jim", "age": 40},
        {"name": "pam", "age": 37}
    ]
    names = pluck("name")
    assert names(people) == ["jim", "pam"]