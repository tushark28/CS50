def main():
    greet = input("Greeting: ")
    greet = value(greet)
    print(greet)


def value(greet):
    array = greet.strip(" ").lower().split(" ")
    first = array[0]
    if first.find("hello") !=-1 :
        return "$0"
    elif first[0] == 'h':
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()