import pytest
import json
import csv
from functionaltools import pipe, abspath, open


def read_json(file):
    return pipe(
        abspath,
        open(json.load)
    )(file)

def read_csv(file):
    return pipe(
        abspath,
        open(pipe(csv.reader, list))
    )(file)


@pytest.fixture
def json_data():
    return read_json("tests/data/sample.json")


@pytest.fixture
def csv_data():
    return read_csv("tests/data/sample.csv")


def test_json_output(json_data):
    assert json_data[0].get("name") == "jim"


def test_csv_output(csv_data):
    assert csv_data[0][0] == "name"