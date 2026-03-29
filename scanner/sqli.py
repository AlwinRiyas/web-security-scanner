import requests

def test_sqli(url):
    payload = "' OR 1=1 --"
    test_url = url + "?id=" + payload

    res = requests.get(test_url)

    if "sql" in res.text.lower() or "error" in res.text.lower():
        return True
    return False