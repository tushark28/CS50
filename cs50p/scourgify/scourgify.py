import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) <3:
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

reader = csv.DictReader(file)
new =[]
for line in reader:
    last,first = line["name"].split(",")
    new.append({"first":first.lstrip() , "last":last, "house":line["house"]})

file.close()

with open(sys.argv[2],"w") as file:
    writer = csv.DictWriter(file,fieldnames=["first","last","house"])
    writer.writeheader(0)
    for line in new:
        writer.writerow({"first" : line["first"], "last":line["last"],"house":line["house"]})