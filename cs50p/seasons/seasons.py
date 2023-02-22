import datetime
import sys
import num2words

def main():
    print(okay(input("Date of Birth: ")))


def okay(birth):
    today = datetime.datetime.today()
    try:
        year,month,day = birth.split("-")
        then = datetime.datetime(int(year),int(month),int(day))
    except (SyntaxError,ValueError):
        sys.exit()
    ans = int((today-then).days)
    return f"{num2words.num2words(ans*24*60)} minutes"


if __name__ == "__main__":
    main()