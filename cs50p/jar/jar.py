class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f'{"🍪"*self.size}'

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if 0 > (size + self.size) > self.capacity:
            raise ValueError
        self._size = size

def main():
    jar = Jar(15)
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)
    jar.deposit(15)
    print(jar)


if __name__ == "__main__":
    main()