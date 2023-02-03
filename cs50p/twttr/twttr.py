string = input("Input: ")
print("Output: ",end="")
for s in string:
    if s.lower() == 'a' or s.lower() == 'e' or s.lower() == 'i' or s.lower() == 'o' or s.lower() == 'u':
        continue
    else:
        print(s,end="")
print()