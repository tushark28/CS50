import random
while True:
    level = input("Level: ")
    if not level.isdigit():
        continue
    elif not 0 < int(level) <0 100:
        continue
    else:
        level = int(level)
        level = random.randint(1,level)
        break
while True:
    guess = input("Guess: ")
    if not guess.isdigit():
        continue
    else:
        guess = int(guess)
        if level>guess:
            print("Too small!")
            continue
        elif level<guess:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
