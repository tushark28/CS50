# TODO

from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    coin = 0
    if (change>=25 and change!=0):
        coin += change%0.25
        change = change - coin*0.25

    print(coin)

