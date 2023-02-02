camel = input("camelCase: ")

print("snake_case: ",end="")

for i in camel:
    if not i.isupper():
        print(i,end="")
    else:
        print(f"_{i.lower()}",end="")

print()