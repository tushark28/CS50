import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) <2:
    sys.exit("Too few command-line arguments")

try:
    if sys.argv[1].split(".")[1] != "py":
        sys.exit("Not a python file")
except ValueError:
    sys.exit("Not a python file")
