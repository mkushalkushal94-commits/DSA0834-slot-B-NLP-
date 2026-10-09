import re


# --------------------------------------------------
# Read text file
# --------------------------------------------------
def load_text(filename):

    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ""


# --------------------------------------------------
# Word Search
# --------------------------------------------------
def word_search(text, word):

    pattern = r"\b" + re.escape(word) + r"\b"

    return re.findall(
        pattern,
        text,
        re.IGNORECASE
    )


# --------------------------------------------------
# Prefix Search
# --------------------------------------------------
def prefix_search(text, prefix):

    words = re.findall(
        r"\b[A-Za-z]+\b",
        text
    )

    matches = []

    for word in words:

        if word.lower().startswith(
            prefix.lower()
        ):
            matches.append(word)

    return matches


# --------------------------------------------------
# Suffix Search
# --------------------------------------------------
def suffix_search(text, suffix):

    words = re.findall(
        r"\b[A-Za-z]+\b",
        text
    )

    matches = []

    for word in words:

        if word.lower().endswith(
            suffix.lower()
        ):
            matches.append(word)

    return matches


# --------------------------------------------------
# Date Search
# --------------------------------------------------
def date_search(text):

    pattern = (
        r"\b"
        r"(?:0[1-9]|[12]\d|3[01])"
        r"/"
        r"(?:0[1-9]|1[0-2])"
        r"/"
        r"\d{4}"
        r"\b"
    )

    return re.findall(pattern, text)


# --------------------------------------------------
# Phone Number Search
# --------------------------------------------------
def phone_search(text):

    pattern = r"\b[6-9]\d{9}\b"

    return re.findall(pattern, text)


# --------------------------------------------------
# Hashtag Search
# --------------------------------------------------
def hashtag_search(text):

    pattern = r"#[A-Za-z0-9_]+"

    return re.findall(pattern, text)


# --------------------------------------------------
# Mention Search
# --------------------------------------------------
def mention_search(text):

    pattern = r"@[A-Za-z0-9_]+"

    return re.findall(pattern, text)


# --------------------------------------------------
# Display Results
# --------------------------------------------------
def display_results(title, results):

    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)

    if results:

        for item in results:
            print(item)

        print("\nTotal Matches:", len(results))

    else:

        print("No matching patterns found.")
        print("Total Matches: 0")


# --------------------------------------------------
# Main Program
# --------------------------------------------------

text = load_text("Q3_text_data.txt")

if not text:
    exit()


print("=" * 65)
print("             SMART PATTERN MATCHING ENGINE")
print("=" * 65)


while True:

    print("\nMENU")
    print("-" * 30)

    print("1. Search Word")
    print("2. Search Date")
    print("3. Search Phone Number")
    print("4. Search Hashtag")
    print("5. Search Mention")
    print("6. Search Prefix")
    print("7. Search Suffix")
    print("8. Exit")


    choice = input(
        "\nEnter your choice: "
    ).strip()


    # Word Search
    if choice == "1":

        word = input(
            "Enter word to search: "
        ).strip()

        if word:

            results = word_search(
                text,
                word
            )

            display_results(
                "WORD SEARCH",
                results
            )

        else:

            print("Invalid word.")


    # Date Search
    elif choice == "2":

        results = date_search(text)

        display_results(
            "DATE SEARCH",
            results
        )


    # Phone Search
    elif choice == "3":

        results = phone_search(text)

        display_results(
            "PHONE NUMBER SEARCH",
            results
        )


    # Hashtag Search
    elif choice == "4":

        results = hashtag_search(text)

        display_results(
            "HASHTAG SEARCH",
            results
        )


    # Mention Search
    elif choice == "5":

        results = mention_search(text)

        display_results(
            "MENTION SEARCH",
            results
        )


    # Prefix Search
    elif choice == "6":

        prefix = input(
            "Enter prefix: "
        ).strip()

        if prefix:

            results = prefix_search(
                text,
                prefix
            )

            display_results(
                "PREFIX SEARCH",
                results
            )

        else:

            print("Invalid prefix.")


    # Suffix Search
    elif choice == "7":

        suffix = input(
            "Enter suffix: "
        ).strip()

        if suffix:

            results = suffix_search(
                text,
                suffix
            )

            display_results(
                "SUFFIX SEARCH",
                results
            )

        else:

            print("Invalid suffix.")


    # Exit
    elif choice == "8":

        print(
            "\nPattern matching engine closed."
        )

        break


    else:

        print(
            "Invalid choice. "
            "Please select 1-8."
        )
