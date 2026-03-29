import requests

def check_headers(url):
    res = requests.get(url)
    headers = res.headers

    results = {
        "CSP": "Content-Security-Policy" in headers,
        "X-Frame": "X-Frame-Options" in headers,
        "XSS": "X-XSS-Protection" in headers
    }

    return results