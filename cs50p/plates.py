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
        if i == ' ' or i == '.' or i ==',':
            return False
        if i.isalpha():
            continue
        if i.isdigit():
            break

    if char_count < 1:
        return False

    for i in range(char_count,len(s)):
        if i == ' ' or i == '.' or i ==',':
            return False
        if not s[i].isdigit():
            return False
    return True

main()