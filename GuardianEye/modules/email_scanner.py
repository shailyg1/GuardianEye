import re

def scan_email(email_text):
    suspicious_keywords = ['urgent', 'password', 'verify', 'update', 'click here', 'reset']
    result = {"Suspicious Keywords": [], "Phishing Links": []}
    for kw in suspicious_keywords:
        if kw in email_text.lower():
            result["Suspicious Keywords"].append(kw)
    urls = re.findall(r'(https?://\S+)', email_text)
    # Simple phishing indicator: Look for long domains, punycode, or IP addresses
    for url in urls:
        if re.search(r'xn--|://\d+\.\d+\.\d+\.\d+|.{40,}', url):
            result["Phishing Links"].append(url)
    if not result["Suspicious Keywords"] and not result["Phishing Links"]:
        return "No obvious threats detected."
    return result
