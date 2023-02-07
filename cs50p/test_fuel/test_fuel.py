from fuel import gauge,convert
import pytest
def main():
    test_convert_zero()
    test_convert_big()
    test_gauge_99()
    test_gauge_1()
    test_gauge_normal()

def test_convert_zero():
    with pytest. convert("5/0")