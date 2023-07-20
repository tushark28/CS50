from data import format_data

def test_data():
    assert format_data("google", "noname@gmail.com", "FuckU") == {'google': [{'email': 'noname@gmail.com', 'pass': 'FuckU'}]}

    assert format_data("google", "tushar@gmail.com", "1234") == {'google': [{'email': 'tushar@gmail.com', 'pass': '1234'}]}

    assert format_data("google", "samar@gmail.com", "!@#$%") == {'google': [{'email': 'samar@gmail.com', 'pass': "!@#$%"}]}

    assert format_data("bgmi", "iamtktushar@gmail.com", "GOD_IGL") == {'bgmi': [{'email': 'iamtktushar@gmail.com', 'pass': 'GOD_IGL'}]}
