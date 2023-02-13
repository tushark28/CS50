import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) <3:
    sys.exit("Too few command-line arguments")

try:
    if ".jpg" not in sys.argv[1].lower() and ".jpeg" not in sys.argv[1].lower() and ".png" not in sys.argv[1].lower():
        sys.exit("Invalid Input")
    if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit()
    file = open(sys.argv[1],"r")
except ValueError:
    sys.exit("Not a csv file")
except IndexError:
    sys.exit("Not a csv file")
except FileNotFoundError:
    sys.exit("File does not Exist")
