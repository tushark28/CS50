import random
while True:
    level = input("Level: ")
    if not level.isdigit():
        continue
    else:
        level = random.getint()