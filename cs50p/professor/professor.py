import random


def main():
    level = get_level()
    count = 0
    for i in range(10):
        flag = 0
        int1 = generate_integer(level)
        int2 = generate_integer(level)
        for j in range(3):
            try:
                ans = input(f"{int1} + {int2} = ")
            except ValueError:
                print("EEE")
                continue
            if ans == int1 + int2:
                count += 1
                break
            else:
                print("EEE")
                flag +=1

        if flag == 3:
            print(f"{int1} + {int2} = {int1 + int2}")


def get_level():
    try:
        level = int(input("Level: "))
        if not 1<=level <=3:
            return get_level()
        else:
            return level
    except ValueError:
        return get_level()



def generate_integer(level):
    if level == 1:
        random.randint()


if __name__ == "__main__":
    main()