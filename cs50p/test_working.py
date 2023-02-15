from working import convert
import pytest

def main():
    test_correct()
    test_wrong()
    test_cat()

def test_correct():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_cat():
    with pytest.raises(ValueError):
        convert("cat")

def test_wrong():
    with pytest.raises(ValueError):
        convert("13 AM to 21 PM")