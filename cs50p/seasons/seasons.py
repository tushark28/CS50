from datetime import date
import sys

def main():
    birth = input("Date of Birth: ")
    print(date.today())
    year,month,day = birth.split("-")
    try:
        print(date(2001,6,1))

if __name__ == "__main__":
    main()