while True:
    fuel = input("Fraction: ")
    try:
        x,y = fuel.split("/")
        x = int(x)
        y = int(y)
        if x>y:
            continue
        

