from scanner.basic import check_status
from scanner.headers import check_headers
from scanner.sqli import test_sqli
from scanner.xss import test_xss
from utils.reporter import print_report

print("==============================")
print(" WEB SECURITY TOOLKIT 🔐")
print("==============================")

url = input("Enter URL: ")

basic = check_status(url)

if "error" in basic:
    print_report(basic)
else:
    headers = check_headers(url)
    sqli = test_sqli(url)
    xss = test_xss(url)

    result = {
        "status": basic["status"],
        "server": basic["server"],
        "headers": headers,
        "sqli": sqli,
        "xss": xss
    }

    print_report(result)