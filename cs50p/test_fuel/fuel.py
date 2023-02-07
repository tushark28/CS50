def main():
    fuel = input("Fraction: ")
    fuel = convert(fuel)
    ans = gauge(fuel)
    print(ans)

def convert(fuel):
    x,y = fuel.split("/")
    x = int(x)
    y = int(y)
    if y==0:
        raise ZeroDivisionError
    if x>y:
        raise ValueError
    return round(x/y *100)

def gauge(per):
    if per<=1:
        return ("E")
    elif per>=99:
        return ("F")
    else:
        return (f"{per}%")

if __name__ == "__main__":
    main()