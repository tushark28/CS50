from plates import is_valid

def main():
    test_cs05()
    test_cs50()
    test_PI314()
    test_h()
    test_outatime()


def test_cs05():
    assert is_valid("cs05") == False

def test_cs50():
    assert is_valid("cs50") == True

def test_PI314():
    assert is_valid("PI3.14") == False

def test_h():
    assert is_valid("h") == False

def test_outatime():
    assert is_valid("OUTATIME") == False

def test_number():
    assert is_valid("96904") == False

def test_place():
    assert is_valid("ab86a") == False

if __name__ == "__main__":
    main()