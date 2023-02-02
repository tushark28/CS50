i = 0
while i<50:
    print(f"Amount Due: {50-i}")
    new = int(input("Insert coin: "))
    i += new

print(f"Change Owed: {i-50}")