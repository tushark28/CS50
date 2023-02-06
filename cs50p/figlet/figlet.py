import pyfiglet
import sys

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        try:
            f=pyfiglet.Figlet(font=sys.argv[2])
        except FontNotFound(sys.argv[2]):
            sys.exit("Invalid Usage")
        user = input("Input: ")
        print("Output: ")
        print(f.renderText(user))
    else:
        sys.exit("Invalid Usage")
else:
    user = input("Input: ")
    print("Output: ")
    f=pyfiglet.Figlet()
    print(f.renderText(user))
