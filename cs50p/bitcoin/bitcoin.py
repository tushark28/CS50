import requests, sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument ")

try:
    coin = int(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")
    
