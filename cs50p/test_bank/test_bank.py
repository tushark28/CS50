from bank import value

def main():
    test()

def test():
    assert value("hey") == "$20"
    assert value("what's up") == "$100"
    assert value("HELLO") == "$0"
