import pytest
from app1 import translate

def test_word_in_dict():
    assert translate("rain") ==  (['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in drops of water.'])

def test_word_not_in_dict():
    ans = "The word doesn't exist. Please double check it."
    assert translate("dddd") == ans

def test_word_uppercase():
    ans = (['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in drops of water.'])
    assert translate("RAIN") == ans

def test_word_mixedcase():
    ans = (['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in drops of water.'])
    assert translate("Rain") == ans

def test_empty_word():
    ans = "The word doesn't exist. Please double check it."
    assert translate("") == ans

def test_space_word():
    ans = "The word doesn't exist. Please double check it."
    assert translate(" ") == ans
