import validators

def main():
    print(count(input("What's your email address? ")))


def count(s):
    matches = re.findall(r"(?:[ ]|^)um([, ?]|[^a-z]|$)",s.lower())
    return len(matches)



if __name__ == "__main__":
    main()