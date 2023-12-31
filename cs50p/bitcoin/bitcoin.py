import requests, sys, json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument ")

try:
    coin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = float(response.json()["bpi"]["USD"]["rate"].replace(",","")) * float(sys.argv[1])
    response = float(f"{response:4f}")
    print("$",f"{response:,}",sep="")
except requests.RequestException:
    sys.exit()

