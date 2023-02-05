months=[
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
        x,y,z = date.split("/")
        if len(z) != 4 or int(x) > 31 or int(y) > 12:
            continue

        print(f"{int(z)}-{int(y):02d}-{int(x):02d}")
    except ValueError:
            x,y,z = date.split(" ")
            if y[-1]!=',' or (x not in months) or len(z)!=4:
                continue
            if int(y[:-1])>31:
                continue
            print(f"{int(z)}-{(months.index(x) + 1):02d}-{int(y[-1]):02d}")

