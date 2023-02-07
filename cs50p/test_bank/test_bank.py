from bank import value

def main():
    test_20()
    test_full()
    test_0()
    test_insens()

def test_20():
    assert value("hey") == 20
def test_full():
    assert value("what's up") == 100
def test_0():
    assert value("HELLO") == 0
def test_insens():
    assert value("hElLo") == 0

if __name__ == "__main__":
    main()