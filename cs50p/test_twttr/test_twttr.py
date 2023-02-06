from twttr import shorten
def main():
    test_twttr_lower()
    test_twttr_upper()
def test_twttr():
    assert shorten("twitter") == "twttr"

if __name__ == "__main__":
    main()