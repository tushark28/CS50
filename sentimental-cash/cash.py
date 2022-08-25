# TODO

from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change>=0:
        break

coin = 0

if (change >= 0.25 and change != 0):
    coin += change//0.25
    change = change - coin * 0.25

if (change >= 0.10 and change != 0):
    tens = change // 0.10
    coin += tens
    change = change - tens * 0.10

if (change >= 0.05 and change != 0):
    fives = change // 0.05
    coin += fives
    change = change - fives * 0.05

if (change >= 0.01 and change != 0):
    ones = change // 0.01
    coin += ones
    change = change - ones * 0.01

print(coin)

