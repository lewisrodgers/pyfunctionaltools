import pytest
from functionaltools import all, equals    
    

def test_truthy():
    return all(equals(1), [1, 1]) == True

def test_falsey():
    return all(equals(1), [1, 2]) == False
