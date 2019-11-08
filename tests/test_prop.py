import pytest
from functionaltools import prop


@pytest.fixture
def props():
    return {
        "name": "Bob",
        "age": 30
    }


def test_prop(props):
    name = prop("name")
    age = prop("age")
    assert name(props) == "Bob"
    assert age(props) == 30