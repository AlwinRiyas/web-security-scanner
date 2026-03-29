def print_report(data):
    print("\n===== SCAN REPORT =====")

    if "error" in data:
        print("Error:", data["error"])
        return

    print("Status Code:", data["status"])
    print("Server:", data["server"])

    print("\nSecurity Headers:")
    for k, v in data["headers"].items():
        print(f"{k}: {'Present' if v else 'Missing'}")

    print("\nSQL Injection:", "Vulnerable" if data["sqli"] else "Safe")
    print("XSS:", "Vulnerable" if data["xss"] else "Safe")