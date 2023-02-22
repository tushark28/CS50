from datetime import date
import sys
import re
import inflect


engine = inflect.engine()
def main():
    print(okay(input("Date of Birth: ")))


def okay(birth):
    today = date.today()
    try:
        year,month,day = birth.split("-")
        then = date(int(year),int(month),int(day))
    except (SyntaxError,ValueError):
        sys.exit("Invalid Date")
    ans = int((today-then).days)
    return f"{num2words.num2words(ans*24*60)} minutes"


if __name__ == "__main__":
    main()