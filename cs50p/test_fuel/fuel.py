while True:
    fuel = input("Fraction: ")
    try:
        x,y = fuel.split("/")
        x = int(x)
        y = int(y)
        if x>y:
            continue
        if y==0:
            continue
    except ValueError:
        pass
    else:
        break

per = round(x/y *100)

if per<=1:
    print("E")
elif per>=99:
    print("F")
else:
    print(f"{per}%")

