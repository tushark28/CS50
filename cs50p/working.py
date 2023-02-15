import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"([0-9]+)(:[0-9]+)? (AM|PM) to ([0-9]+)(:[0-9]+)? (AM|PM)",s):
        print(matches.groups())
        if not 1<= int(matches.group(1)) <= 12:
            raise ValueError

        if matches.group(2) != None:
            if not 0<=int(matches.group(2))<=59:
                raise ValueError
        print(matches.group(3), 'AM')
        if matches.group(3) != 'AM' or matches.group(3) != 'PM':
            raise ValueError

        if not 1<= int(matches.group(4)) <= 12:
            raise ValueError

        if matches.group(5) != None:
            if not 0<=int(matches.group(5))<=59:
                raise ValueError

        if matches.group(6) != 'AM' or matches.group(6) != 'PM':
            raise ValueError




if __name__ == "__main__":
    main()