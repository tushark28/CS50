import datetime
import sys

def main():
    # birth = input("Date of Birth: ")
    print(datetime.date.today())
    # year,month,day = birth.split("-")
    try:
        print(datetime.datetime(2001,6,1))

if __name__ == "__main__":
    main()