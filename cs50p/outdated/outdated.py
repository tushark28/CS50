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
        try:
            x,y,z = date.split("/")
            if len(z) != 4 or int(x) > 31 or int(y) > 12:
                continue

            print(f"{int(z)}-{int(y):02d}-{int(x):02d}")
        except ValueError:
            try:

