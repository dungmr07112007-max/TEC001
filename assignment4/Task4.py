import re

def redact_phone_numbers(text):
    pattern = r'(\b\d{10}\b|\+84\d+)'
    return re.sub(pattern, '[REDACTED]', text)

text = input("Enter text: ")
result = redact_phone_numbers(text)
print("Result:", result)