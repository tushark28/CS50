import sys
import csv

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) <2:
    sys.exit("Too few command-line arguments")

try:
    if sys.argv[1].split(".")[1] != "csv":
        sys.exit("Not a csv file")
    file = open(sys.argv[1],"r")
except ValueError:
    sys.exit("Not a csv file")
except IndexError:
    sys.exit("Not a csv file")
except FileNotFoundError:
    sys.exit("File does not Exist")

reader = csv.DictReader()