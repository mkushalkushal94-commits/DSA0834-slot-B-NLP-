import re


# --------------------------------------------------
# Validate Email
# --------------------------------------------------
def validate_email(email):

    pattern = (
        r"^[A-Za-z]"
        r"[A-Za-z0-9._]*"
        r"@"
        r"[A-Za-z]+"
        r"\."
        r"(?:com|org|edu|net|in)$"
    )

    return bool(re.fullmatch(pattern, email))


# --------------------------------------------------
# Validate Password
# --------------------------------------------------
def validate_password(password):

    pattern = (
        r"^(?=.*[A-Z])"
        r"(?=.*[a-z])"
        r"(?=.*\d)"
        r"(?=.*[@#$%&!])"
        r".{8,}$"
    )

    return bool(re.fullmatch(pattern, password))


# --------------------------------------------------
# Validate Mobile Number
# --------------------------------------------------
def validate_mobile(mobile):

    pattern = r"^[6-9]\d{9}$"

    return bool(re.fullmatch(pattern, mobile))


# --------------------------------------------------
# Read users from dataset
# --------------------------------------------------
def load_users(filename):

    try:
        with open(filename, "r") as file:
            data = file.read()

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

    records = re.split(r"\n\s*\n", data.strip())

    users = []

    for record in records:

        name_match = re.search(
            r"Name\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )

        email_match = re.search(
            r"Email\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )

        password_match = re.search(
            r"Password\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )

        mobile_match = re.search(
            r"Mobile\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )

        user = {
            "name": name_match.group(1).strip()
            if name_match else "",

            "email": email_match.group(1).strip()
            if email_match else "",

            "password": password_match.group(1).strip()
            if password_match else "",

            "mobile": mobile_match.group(1).strip()
            if mobile_match else ""
        }

        users.append(user)

    return users


# --------------------------------------------------
# Display validation result
# --------------------------------------------------
def display_status(field, status):

    if status:
        print(f"{field:<20}: VALID")
    else:
        print(f"{field:<20}: INVALID")


# --------------------------------------------------
# Main Program
# --------------------------------------------------

users = load_users("Q1_user_credentials.txt")

if not users:
    exit()


print("=" * 65)
print("       INTELLIGENT USER CREDENTIAL VALIDATOR")
print("=" * 65)

valid_users = 0
invalid_users = 0


for number, user in enumerate(users, start=1):

    email_valid = validate_email(user["email"])

    password_valid = validate_password(user["password"])

    mobile_valid = validate_mobile(user["mobile"])

    all_valid = (
        email_valid
        and password_valid
        and mobile_valid
    )

    print(f"\nUSER {number}")
    print("-" * 65)

    print("Name     :", user["name"])
    print("Email    :", user["email"])
    print("Password :", "*" * len(user["password"]))
    print("Mobile   :", user["mobile"])

    print("\nValidation Results")

    display_status("Email", email_valid)
    display_status("Password", password_valid)
    display_status("Mobile Number", mobile_valid)

    if all_valid:
        print("\nAccount Status : VALID")
        valid_users += 1
    else:
        print("\nAccount Status : INVALID")
        invalid_users += 1


# --------------------------------------------------
# Final Report
# --------------------------------------------------

print("\n" + "=" * 65)
print("                    FINAL REPORT")
print("=" * 65)

print("Total Users   :", len(users))
print("Valid Users   :", valid_users)
print("Invalid Users :", invalid_users)

print("\nCredential validation completed.")
