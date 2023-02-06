import requests, sys, json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument ")

try:
    coin = int(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(json.dumps(response.json(),indent = 4))
except requests.RequestException:
    pass

