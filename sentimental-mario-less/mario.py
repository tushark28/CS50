# TODO
from cs50 import get_int
height = get_int("Height: ")
for i in range(height):
    print((height-i-1)*' ',end="")
    print((i+1)*"#")