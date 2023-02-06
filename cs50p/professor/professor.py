import random


def main():
    level = get_level()
    


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
    pass


if __name__ == "__main__":
    main()