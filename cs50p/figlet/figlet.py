import pyfiglet
import sys

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        f=pyfiglet.Figlet()
        fonts = f.getFonts()

        if sys.argv[2] not in fonts:
            sys.exit("Invalid Usage")
        f.setFont(font=sys.argv[2])
        user = input("Input: ")
        print("Output: ")
        print(f.renderText(user))

    else:
        sys.exit("Invalid Usage")
elif len(sys.argv) == 1:
    user = input("Input: ")
    print("Output: ")
    f=pyfiglet.Figlet()
    print(f.renderText(user))
