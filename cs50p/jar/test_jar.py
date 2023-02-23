from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3

def test_str():
    jar3 = Jar()
    assert str(jar3) == ""
    jar3.deposit(1)
    assert str(jar3) == "🍪"
    jar3.deposit(11)
    assert str(jar3) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar4 = Jar(5)
    jar4.deposit(2)
    assert jar4.size == 2

def test_withdraw():
    jar5 = Jar(4)
    jar5.deposit(4)
    jar5.withdraw(3)
    assert jar5.size == 1

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

if __name__ == "__main__":
    main()
