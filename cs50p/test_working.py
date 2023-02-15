import convert from working

def main():
    test_correct()
    test_wrong()
    test_cat()

def test_correct():
    assert convert("9:00 AM to 5:00 PM") == 