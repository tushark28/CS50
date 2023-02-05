items = {}
while True:
    try:
        try:
            item = input()
            items[item] +=1
        except KeyError:
