import re

def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"um[^a-zA-Z0-9]?",s)
    print(matches)



if __name__ == "__main__":
    main()