import random
while True:
    level = input("Level: ")
    if not level.isdigit():
        continue
    else:
        level = random.randint(1,level)
        break
while True:
    guess = input("Guess: ")
    if not guess.isdigit():
        continue
    else:
        if level>guess:
            print("Too small!")
            continue
        elif level<guess:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
