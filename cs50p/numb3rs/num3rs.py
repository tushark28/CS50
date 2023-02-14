import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        print(match.groups(1))
        print(match.groups(2))
        print(match.groups(3))
        print(match.groups(4))
        if not 0<=int(match.groups(1)) <=255:
            return False
        if not 0<=int(match.groups(2)) <=255:
            return False
        if not 0<=int(match.groups(3)) <=255:
            return False
        if not 0<=int(match.groups(4)) <=255:
            return False
        return True
    else:
        False





if __name__ == "__main__":
    main()