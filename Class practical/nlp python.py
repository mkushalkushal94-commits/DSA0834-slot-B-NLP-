import re

text = "My phone number is 9876543210 and my email is example@gmail.com."

# Search for a 10-digit phone number
phone = re.search(r'\b\d{10}\b', text)

# Search for an email address
email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

if phone:
    print("Phone number found:", phone.group())

if email:
    print("Email address found:", email.group())

