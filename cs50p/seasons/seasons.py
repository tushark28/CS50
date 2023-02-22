from datetime import date
import sys

def main():
    # birth = input("Date of Birth: ")
    print(date.today())
    print(date.fromtimestamp(date.fromisoformat('2001-06-28')))

if __name__ == "__main__":
    main()