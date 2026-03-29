import requests

def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    test_url = url + "?q=" + payload

    res = requests.get(test_url)

    if payload in res.text:
        return True
    return False