import datetime
import sys

def main():
    # birth = input("Date of Birth: ")
    print(datetime.datetime.today())
    # year,month,day = birth.split("-")
    try:
        print(datetime.datetime(2001,6,1))
    except:
        pass


if __name__ == "__main__":
    main()