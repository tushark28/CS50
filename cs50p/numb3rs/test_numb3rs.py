from numb3rs import validate

def main():
    test_ok()
    test_wrong()
    test_cat()

def test_ok():
    assert validate("23.45.68.67") == True

def test_wrong():
    assert validate("23.295.563.294") == False

def test_cat():
    assert validate("cat") == False

def test_5():
    assert validate("23.45.32.23.32") == False

if __name__ == "__main__":
    main()