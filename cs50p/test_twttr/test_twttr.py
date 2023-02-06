from twttr import shorten
def main():
    test_twttr_lower()
    test_twttr_upper()
    test_twttr_punctuation()
    test_twttr_number()

def test_twttr_lower():
    assert shorten("twitter") == "twttr"
def test_twttr_upper():
    assert shorten("TWITTER") == "TWTTR"
def test_twttr_punctuation():
    assert shorten("tushar, is") == "tshr, s"
def test_twttr_number():
    assert shorten("tushar 123") == "tshr 123"


if __name__ == "__main__":
    main()