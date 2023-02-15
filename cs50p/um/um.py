import re

def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"um([, ?]|[^a-z])",s)
    print(matches)



if __name__ == "__main__":
    main()