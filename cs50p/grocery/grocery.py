items = {}
while True:
    try:
        item = input()
        try:
            items[item] +=1
        except KeyError:
            items[item] = 1
    except EOFError:
        items.sort()
        for item in items:
            print(f"{items[item]} {item.upper()}")
        break
