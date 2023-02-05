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
    try:
        date = input("Date: ")
        x,y,z = date.split("/")
        if len(z) != 4:
            continue
        print(f"{int(z)}-{int(y):02d}-{int(x):02d}")
    except ValueError:
        pass
