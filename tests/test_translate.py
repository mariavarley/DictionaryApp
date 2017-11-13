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

def test_word_nonlist():
    ans = ['The science that deals with concepts such as quantity, structure, space and change.']
    assert translate("mathematics") == ans

def test_noun_word():
    ans = (['The capital and largest city of France.'])
    assert translate("Paris") == ans

#def test_close_word():
#    ans = "Did you mean rain? Type Y for yes or N for no"
#    assert translate("rainn") == ans
