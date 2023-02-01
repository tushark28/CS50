def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y)/60.0
    time = round(float(x + y),2)
    return time


if __name__ == "__main__":
    main()