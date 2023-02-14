import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^([0-9])\.([0-9])\.([0-9])\.([0-9])$",ip):
        if not 0<=match.groups(1) <=255:
            return False
        if not 0<=match.groups(2) <=255:
            return False
        if not 0<=match.groups(3) <=255:
            return False
        if not 0<=match.groups(4) <=255:
            return False
        return True
    else:
        False





if __name__ == "__main__":
    main()