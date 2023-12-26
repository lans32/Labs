from main import Levenshtein
import pytest

@pytest.fixture
def lev():
    return Levenshtein()

def test_distance_equal_strings(lev):
    assert lev.levenshtein_distance("kitten", "kitten") == 0

def test_distance_different_strings(lev):
    assert lev.levenshtein_distance("kitten", "sitting") == 3

def test_distance_empty_string(lev):
    assert lev.levenshtein_distance("", "abc") == 3

if __name__ == '__main__':
    pytest.main()