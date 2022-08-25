# TODO
from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

for i in range(height):
    # for spaces.
    print((height-i-1)*' ', end="")
    # for "#" symbol
    print((i+1)*"#")
    # for two spaces
    print("  ", end="")