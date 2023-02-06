import pyfiglet
import sys

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        user = input("Input: ")
        print("Output: ")
        f=pyfiglet.figlet()
        print(f.renderText(user))
    else:
        sys.exit()
