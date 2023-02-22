import datetime
import sys
import num2words

def main():
    birth = input("Date of Birth: ")
    today = datetime.datetime.today()
    try:
        year,month,day = birth.split("-")
        then = datetime.datetime(int(year),int(month),int(day))
    except SyntaxError:
        sys.exit()
    ans = int((today-then).days)
    print(num2words.num2words(ans*24*60), "minutes")

if __name__ == "__main__":
    main()