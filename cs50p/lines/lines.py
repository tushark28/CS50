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

count = 0
for line in file:
    print(f"{len(line)} and \n {len(line)*'.'}")
    if line[0] == '#':
        continue
    elif line == len(line)*" ":
        continue
    else:
        count+=1

print(count)
file.close()