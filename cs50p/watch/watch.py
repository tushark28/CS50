import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if match := re.search(r"<iframe (?:width=\"[0-9]+\" )?(?:height=\"[0-9]+\" )?src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)\" (?:title=\"[^\"]+\" )?(?:frameborder=\"[0-9]+\" )?(?:allow=\"(?:accelerometer; )?(?:autoplay; )?(?:clipboard-write; )?(?:encrypted-media; )?(?:gyroscope; )(?:picture-in-picture)?\" )?(?:allowfullscreen)?></iframe>",s):
        return "https://youtu.be/"+match.groups(1)[0]
    else:
        return None

if __name__ == "__main__":
    main()