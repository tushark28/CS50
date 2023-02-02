i = 0
while i<50:
    print(f"Amount Due: {50-i}")
    new = int(input("Insert coin: "))
    if new == 25 or new == 10 or new == 5:
        i += new

print(f"Change Owed: {i-50}")