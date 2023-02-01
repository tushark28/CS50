def main():
    time = input("What time is it? ")
    convert(time)


def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y)/60.0
    time = float(x + y)
    return time


if __name__ == "__main__":
    main()