def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    char_count = 0
    total_count = 0
    for i in s:
        char_count+=1
        total_count+=1
        if i == ' ' or i == '.' or i ==',':
            return False
        if i.isalpha():
            continue
        if i.isdigit():
            break

    if char_count < 2:
        return False
    if s[char_count] == '0':
        return False

    for i in range(char_count,len(s)):
        total_count+=1
        if i == ' ' or i == '.' or i ==',':
            return False
        if not s[i].isdigit():
            return False
    if not total_count > 6:
        return True

main()