from seasons import okay
import pytest

def main():
    test_1()
    test_2()

def test_1():
    assert okay("2001-06-28") == "Eleven million, three hundred eighty-eight thousand, nine hundred sixty minutes"

def test_2():
    assert okay("2001-06-28") == "Eleven million, three hundred eighty-eight thousand, nine hundred sixty minutes"


if __name__ == "__main__":
    main()