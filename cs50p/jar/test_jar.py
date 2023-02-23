from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 7

def test_withdraw():
    jar = Jar(4)
    jar.withdraw(3)
    assert jar.size == 1

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

if __name__ == "__main__":
    main()
