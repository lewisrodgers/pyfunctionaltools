from functionaltools import pluck


def test_pluck():
    people = [
        {"name": "jim", "age": 40},
        {"name": "pam", "age": 37}
    ]
    names = pluck("name")
    results = names(people)
    assert list(results) == ["jim", "pam"]