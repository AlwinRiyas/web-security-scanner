import requests

def check_status(url):
    try:
        res = requests.get(url)
        return {
            "status": res.status_code,
            "server": res.headers.get("Server")
        }
    except:
        return {"error": "Connection failed"}