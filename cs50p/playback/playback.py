x = input()
array = x.split(" ")

for i in array:
    print(i,end='')
    if not i==array[len(array)-1]:
        print("...",end='')
print()