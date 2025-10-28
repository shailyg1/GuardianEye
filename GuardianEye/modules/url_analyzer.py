import re

def analyze_url(url):
    issues = []
    if re.search(r'xn--', url):  # punycode
        issues.append("Suspicious punycode found.")
    if re.search(r'://\d+\.\d+\.\d+\.\d+', url):  # IP as domain
        issues.append("Domain uses IP address (potential obfuscation).")
    if len(url) > 60:
        issues.append("Excessively long domain.")
    suspicious_keywords = ['login', 'verify', 'password', 'update', 'secure']
    if any(kw in url.lower() for kw in suspicious_keywords):
        issues.append("Suspicious keyword detected.")
    return issues if issues else "URL seems safe."
