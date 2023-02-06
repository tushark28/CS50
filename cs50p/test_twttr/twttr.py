def main():
    string = input("Input: ")
    print("Output: ",end="")
    string = shorten(string)
    print(string)

def shorten(string):
    new=""
    for s in string:
        if s.lower() == 'a' or s.lower() == 'e' or s.lower() == 'i' or s.lower() == 'o' or s.lower() == 'u':
            continue
        else:
            new += s
    return new



if __name__ == "__main__":
    main()