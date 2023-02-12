import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) <2:
    sys.exit("Too few command-line arguments")

try:
    if sys.argv[1].split(".")[1] != "py":
        sys.exit("Not a python file")
    file = open(sys.argv[1],"r")
except ValueError:
    sys.exit("Not a python file")
except IndexError:
    sys.exit("Not a python file")
except FileNotFoundError:
    sys.exit("File does not Exist")

for line in file:
    if line[]

file.close()