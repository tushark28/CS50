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
    line.lstrip(' ')
    if line[0] == '#' or line[0] == '\n':
        continue
    for word in line:
        if word == ' ':
            continue
        else:
            if word == '#':
                break
            else:
                count+=1
                break

print(count)
file.close()