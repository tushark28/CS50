# TODO

from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

coin = 0

# for quarters
if (change >= 0.25 and change != 0):
    coin += change//0.25
    change = round(change % 0.25, 2)

# for dimes
if (change >= 0.10 and change != 0):
    coin += change//0.10
    change = round(change % 0.10, 2)

# for nickel
if (change >= 0.05 and change != 0):
    coin += change//0.05
    change = round(change % 0.05, 2)

# for pennies
if (change >= 0.01 and change != 0):
    coin += change//0.01
    change = round(change % 0.01, 2)

print(int(coin))
