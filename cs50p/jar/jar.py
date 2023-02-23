class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

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
        if 0 > (size):
            raise ValueError
        elif (size) > self.capacity:
            raise ValueError
        self._size = size

def main():
    jar5 = Jar(4)
    jar5.deposit(4)
    jar5.withdraw(3)
    print(jar5.size)


if __name__ == "__main__":
    main()