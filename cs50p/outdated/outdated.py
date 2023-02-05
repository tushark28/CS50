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
        print(f"{z}-{y:02d}-{x:02d}")
    except ValueError:
        pass
