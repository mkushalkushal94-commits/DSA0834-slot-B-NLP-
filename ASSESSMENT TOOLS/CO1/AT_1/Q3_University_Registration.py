import re


# ---------------------------------------------------
# Validate register number
# ---------------------------------------------------
def validate_register_number(register_number):

    pattern = r"^[A-Za-z]{2,4}\d{3,6}$"

    return bool(re.fullmatch(pattern, register_number))


# ---------------------------------------------------
# Validate institutional email
# ---------------------------------------------------
def validate_email(email):

    pattern = r"^[A-Za-z0-9._%+-]+@college\.edu$"

    return bool(re.fullmatch(pattern, email))


# ---------------------------------------------------
# Validate course code
# ---------------------------------------------------
def validate_course_code(course_code):

    pattern = r"^[A-Z]{2,4}\d{3}$"

    return bool(re.fullmatch(pattern, course_code))


# ---------------------------------------------------
# Validate semester
# ---------------------------------------------------
def validate_semester(semester):

    pattern = r"^Semester\s[1-8]$"

    return bool(
        re.fullmatch(
            pattern,
            semester,
            re.IGNORECASE
        )
    )


# ---------------------------------------------------
# Validate mobile number
# ---------------------------------------------------
def validate_mobile(mobile):

    pattern = r"^[6-9]\d{9}$"

    return bool(re.fullmatch(pattern, mobile))


# ---------------------------------------------------
# Read student records from text file
# ---------------------------------------------------
def load_students(filename):

    try:

        with open(filename, "r") as file:
            data = file.read()

    except FileNotFoundError:

        print("Error: student_registration.txt not found.")
        return []


    # Separate individual student records
    records = re.split(r"\n\s*\n", data.strip())

    students = []


    for record in records:

        register_match = re.search(
            r"Register Number\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )

        email_match = re.search(
            r"Email\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )

        course_match = re.search(
            r"Course Code\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )

        semester_match = re.search(
            r"Semester\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )

        mobile_match = re.search(
            r"Mobile\s*:\s*(.+)",
            record,
            re.IGNORECASE
        )


        student = {
            "register": register_match.group(1).strip()
            if register_match else "",

            "email": email_match.group(1).strip()
            if email_match else "",

            "course": course_match.group(1).strip()
            if course_match else "",

            "semester": semester_match.group(1).strip()
            if semester_match else "",

            "mobile": mobile_match.group(1).strip()
            if mobile_match else ""
        }

        students.append(student)


    return students


# ---------------------------------------------------
# Display validation result
# ---------------------------------------------------
def display_status(field, valid):

    if valid:
        print(f"{field:<25}: VALID")
    else:
        print(f"{field:<25}: INVALID")


# ---------------------------------------------------
# Main program
# ---------------------------------------------------

students = load_students("student_registration.txt")

if not students:
    exit()


print("=" * 70)
print("             UNIVERSITY REGISTRATION SYSTEM")
print("=" * 70)


successful = 0
failed = 0


# ---------------------------------------------------
# Validate every student
# ---------------------------------------------------

for number, student in enumerate(students, start=1):

    register_valid = validate_register_number(
        student["register"]
    )

    email_valid = validate_email(
        student["email"]
    )

    course_valid = validate_course_code(
        student["course"]
    )

    semester_valid = validate_semester(
        student["semester"]
    )

    mobile_valid = validate_mobile(
        student["mobile"]
    )


    registration_successful = (
        register_valid
        and email_valid
        and course_valid
        and semester_valid
        and mobile_valid
    )


    print(f"\nSTUDENT {number}")
    print("-" * 70)

    print("Register Number :", student["register"])
    print("Email           :", student["email"])
    print("Course Code     :", student["course"])
    print("Semester        :", student["semester"])
    print("Mobile          :", student["mobile"])

    print("\nValidation Results")

    display_status(
        "Register Number",
        register_valid
    )

    display_status(
        "Institutional Email",
        email_valid
    )

    display_status(
        "Course Code",
        course_valid
    )

    display_status(
        "Semester",
        semester_valid
    )

    display_status(
        "Mobile Number",
        mobile_valid
    )


    if registration_successful:

        print("\nRegistration Status : SUCCESSFUL")
        successful += 1

    else:

        print("\nRegistration Status : FAILED")
        failed += 1


# ---------------------------------------------------
# Final report
# ---------------------------------------------------

print("\n" + "=" * 70)
print("                  FINAL REPORT")
print("=" * 70)

print("Total Registrations :", len(students))
print("Successful          :", successful)
print("Failed              :", failed)

print("\nRegistration processing completed.")
