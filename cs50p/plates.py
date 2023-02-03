def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    char_count = 0
    for i in s:
        char_count+=1
        if i.isalpha():
            continue
        if i.isdigit():
            break:
    for i in range(len(s)):


main()