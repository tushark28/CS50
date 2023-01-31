def main():
    string = input()
    string = convert(string)
    print(string)

def convert(string):
    string = string.replace(":)","🙂")
    string = string.replace(":(","🙁")
    return string

main()