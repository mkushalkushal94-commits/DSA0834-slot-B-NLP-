import re


# ---------------------------------------------------
# Function to extract candidate name
# ---------------------------------------------------
def extract_name(resume):
    pattern = r"Name\s*:\s*(.+)"
    match = re.search(pattern, resume, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return "Not Found"


# ---------------------------------------------------
# Function to extract email
# ---------------------------------------------------
def extract_email(resume):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, resume)

    if match:
        return match.group()

    return "Not Found"


# ---------------------------------------------------
# Function to extract mobile number
# ---------------------------------------------------
def extract_mobile(resume):
    pattern = r"(?:\+91[-\s]?)?[6-9]\d{9}"
    match = re.search(pattern, resume)

    if match:
        return match.group()

    return "Not Found"


# ---------------------------------------------------
# Function to extract technical skills
# ---------------------------------------------------
def extract_skills(resume):
    skills = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "NLP"
    ]

    found_skills = []

    for skill in skills:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, resume, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills


# ---------------------------------------------------
# Function to extract experience
# ---------------------------------------------------
def extract_experience(resume):
    pattern = (
        r"(\d+(?:\.\d+)?)\s*"
        r"(?:years?|yrs?)\s*"
        r"(?:of\s*)?experience"
    )

    match = re.search(pattern, resume, re.IGNORECASE)

    if match:
        return float(match.group(1))

    return 0


# ---------------------------------------------------
# Read resume dataset
# ---------------------------------------------------
try:
    with open("resume_data.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("Error: resume_data.txt file not found.")
    exit()


# ---------------------------------------------------
# Separate individual resumes
# ---------------------------------------------------
resumes = re.split(r"\n\s*\n", data.strip())


print("=" * 70)
print("        RESUME INFORMATION EXTRACTION SYSTEM")
print("=" * 70)


eligible_count = 0


# ---------------------------------------------------
# Process every resume
# ---------------------------------------------------
for number, resume in enumerate(resumes, start=1):

    name = extract_name(resume)
    email = extract_email(resume)
    mobile = extract_mobile(resume)
    skills = extract_skills(resume)
    experience = extract_experience(resume)

    eligible = experience >= 2 and "Python" in skills

    print(f"\nCandidate {number}")
    print("-" * 50)

    print("Name             :", name)
    print("Email            :", email)
    print("Mobile           :", mobile)
    print("Technical Skills :", ", ".join(skills))
    print("Experience       :", experience, "years")

    if eligible:
        print("Eligibility      : ELIGIBLE")
        eligible_count += 1
    else:
        print("Eligibility      : NOT ELIGIBLE")


# ---------------------------------------------------
# Final report
# ---------------------------------------------------
print("\n" + "=" * 70)
print("                    FINAL REPORT")
print("=" * 70)

print("Total Candidates :", len(resumes))
print("Eligible Candidates :", eligible_count)

print("\nEligible Candidates:")

for resume in resumes:

    name = extract_name(resume)
    skills = extract_skills(resume)
    experience = extract_experience(resume)

    if experience >= 2 and "Python" in skills:
        print("-", name)
