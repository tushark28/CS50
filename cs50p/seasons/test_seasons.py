from seasons import okay
import pytest

def main():
    test_1()
    test_2()

def test_1():
    assert okay("2001-06-28") == "eleven million, three hundred and eighty-eight thousand, nine hundred and sixty minutes"

def test_2():
    with pytest.raises(SystemExit):
        okay("dsfsfks")


if __name__ == "__main__":
    main()