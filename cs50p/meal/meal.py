def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y)/60.0
    time = round(float(x + y),1)
    return time


if __name__ == "__main__":
    main()