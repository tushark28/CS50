from fuel import gauge,convert
import pytest
def main():
    test_convert_zero()
    test_convert_big()
    test_gauge_99()
    test_gauge_1()
    test_gauge_normal()
    test_convert_inc()

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_convert_big():
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge_99():
    assert gauge(99) == "F"
    assert convert("1/4") == 25 and gauge(25)== '25%'

def test_gauge_1():
    assert gauge(1) == "E"

def test_gauge_normal():
    assert gauge(75) == "75%"

def test_convert_inc():
    with pytest.raises(ValueError):
        convert("cat/dog")

if __name__ == "__main__":
    main()