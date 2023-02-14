import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        if not 0<=int(match.groups(1)[0]) <=255:
            return False
        if not 0<=int(match.groups(2)[1]) <=255:
            return False
        if not 0<=int(match.groups(3)[2]) <=255:
            return False
        if not 0<=int(match.groups(4)[3]) <=255:
            return False
        return True
    else:
        False


if __name__ == "__main__":
    main()