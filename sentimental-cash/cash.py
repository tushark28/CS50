# TODO

from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change>=0:
        break

coin = 0

if (change >= 0.25 and change != 0):
    coin += change//0.25
    change = round(change % 0.25,2)

if (change >= 0.10 and change != 0):
    coin += change//0.10
    change = round(change % 0.10,2)

if (change >= 0.05 and change != 0):
    coin += change//0.05
    change = round(change % 0.05,2)

if (change >= 0.01 and change != 0):
    coin += change//0.01
    change = change%0.01

print(coin)

