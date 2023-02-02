i = 0
while i<=50:
    print(f"Amount due: {50-i}")
    new = int(input("Insert coin: "))
    i += new

print(f"Change owed: {i-50}")