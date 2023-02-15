from um import count

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert count("cat") == 0

def test_2():
    assert count("um") == 1

def test_3():
    assert count("yummy um um,") == 2


if __name__ == "__main__":
    main()