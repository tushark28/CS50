months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        y, x, z = date.split("/")
        x = int(x)
        y = int(y)
        if len(z) != 4 or x > 31 or int(y) > 12:
            continue

        print(f"{int(z)}-{y:02d}-{x:02d}")
        break

    except ValueError:
        x, y, z = date.split(" ")
        if y[-1] != ',' or (x.lower().title() not in months) or len(z) != 4:
            continue
        if int(y[:-1]) > 31:
            continue
        print(
            f"{int(z)}-{(months.index(x.lower().title()) + 1):02d}-{int(y[:-1]):02d}")
        break
