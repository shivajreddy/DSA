from stencil import *


def test_close_strings():
    assert close_strings("BEARS", "BEAST") == (3, 1)
    assert close_strings("BANANA", "ORANGE") == (0, 2)
    assert close_strings("HELLO", "WORLD") == (1, 1)
    assert close_strings("PYTHON", "JAVASCRIPT") == (0, 2)
    assert close_strings("big", "data") == (0, 0)
    assert close_strings("bear", "beast") == (3, 0)
    assert close_strings("honey", "money") == (4, 0)
    assert close_strings("happy", "sad") == (1, 0)
    assert close_strings("loud", "loud") == (4, 0)
    assert close_strings("sleep", "peels") == (1, 4)
    assert close_strings("train", "rain") == (0, 4)
    assert close_strings("water", "batter") == (2, 2)
    assert close_strings("dress", "rest") == (0, 3)
    assert close_strings("chair", "hairs") == (0, 4)
    assert close_strings("BEACH", "PEACH") == (4, 0)


def test_check_anagram():
    assert check_anagram("listen", "silent") == True
    assert check_anagram("triangle", "integral") == True
    assert check_anagram("apple", "banana") == False
    assert check_anagram("", "") == True
    assert check_anagram("abcd", "dcba") == True
    assert check_anagram("Listen", "silent") == True
    assert check_anagram("inTegRal", "Triangle") == True
