import pyfiglet
import sys

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        user = input("Input: ")
        print("Output: ")
        f=pyfiglet.Figlet(font=sys.argv[2])
        print(f.renderText(user))
    else:
        sys.exit()
else:
    user = input("Input: ")
    print("Output: ")
    f=pyfiglet.Figlet()
    print(f.renderText(user))
