import datetime
import sys

def main():
    # birth = input("Date of Birth: ")
    today = datetime.datetime.today()
    try:
        # year,month,day = birth.split("-")
        then = datetime.datetime(2001,6,1)
    except SyntaxError:
        sys.exit()
    print(int(today-then))


if __name__ == "__main__":
    main()