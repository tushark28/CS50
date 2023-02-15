import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"([0-9]+)(:[0-9]+)? (AM|PM) to ([0-9]+)(:[0-9]+)? (AM|PM)",s):
        if not 1<= int(matches.group(1)) <= 12:
            raise ValueError

        if matches.group(2) != None:
            if not 0<=int(matches.group(2).replace(":",""))<=59:
                raise ValueError

        if not (str(matches.group(3)) == str('AM') or str(matches.group(3)) == str('PM')):
            raise ValueError

        if not 1<= int(matches.group(4)) <= 12:
            raise ValueError

        if matches.group(5) != None:
            if not 0<=int(matches.group(5).replace(":",""))<=59:
                raise ValueError

        if not (str(matches.group(6)) == str('AM') or str(matches.group(6)) == str('PM')):
            raise ValueError

        if str(matches.group(3)) == str('AM'):
            if int(matches.group(1)) == 12:
                time1p1 = "00"
            else:
                time1p1 = f"{int(matches.group(1)):02d}"
        else:
            time1p1 = str(int(matches.group(1))+12)

        if matches.group(2) != None:
            time1p1 += f"{str(matches.group(2))}"
        else:
            time1p1 += ":00"

        if str(matches.group(6)) == str('AM'):
            if int(matches.group(4)) == 12:
                time2p1 = "00"
            else:
                time2p1 = f"{int(matches.group(4)):02d}"
        else:
            time2p1 = str(int(matches.group(4))+12)

        if matches.group(5) != None:
            time2p1 += f"{str(matches.group(5))}"
        else:
            time2p1 += ":00"

        return f"{time1p1} to {time2p1}"

    else:
        raise ValueError



if __name__ == "__main__":
    main()