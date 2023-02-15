import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"([0-9]+)(:[0-9]+)? (AM|PM) to ([0-9]+)(:[0-9]+)? (AM|PM)",s):
        print(matches.groups())
        if not 1<= int(matches.group(1)) <= 12




if __name__ == "__main__":
    main()