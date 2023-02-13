import sys
from PIL import Image,ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) <3:
    sys.exit("Too few command-line arguments")

try:
    if ".jpg" not in sys.argv[1].lower() and ".jpeg" not in sys.argv[1].lower() and ".png" not in sys.argv[1].lower():
        sys.exit("Invalid Input")
    if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Input and Output have different extensions")
    image1 = Image.open(sys.argv[1])
    #image2 = Image.open(sys.argv[2])
    cs50 = Image.open("shirt.png")
except ValueError:
    sys.exit("Invalid Input")
except IndexError:
    sys.exit("Invalid Input")
except FileNotFoundError:
    sys.exit("File does not Exist")

image2 = ImageOps.fit(image1,cs50.size)
image2.paste(cs50)

