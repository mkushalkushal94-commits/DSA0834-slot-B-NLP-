import re


# ---------------------------------------------------
# Function to load products from text file
# ---------------------------------------------------
def load_products(filename):

    try:
        with open(filename, "r") as file:
            products = [
                line.strip()
                for line in file
                if line.strip()
            ]

        return products

    except FileNotFoundError:
        print("Error: Product dataset not found.")
        return []


# ---------------------------------------------------
# Exact keyword search
# ---------------------------------------------------
def exact_search(products, keyword):

    pattern = r"^" + re.escape(keyword) + r"$"

    return [
        product
        for product in products
        if re.search(pattern, product, re.IGNORECASE)
    ]


# ---------------------------------------------------
# Prefix search
# ---------------------------------------------------
def prefix_search(products, keyword):

    pattern = r"^" + re.escape(keyword)

    return [
        product
        for product in products
        if re.search(pattern, product, re.IGNORECASE)
    ]


# ---------------------------------------------------
# Suffix search
# ---------------------------------------------------
def suffix_search(products, keyword):

    pattern = re.escape(keyword) + r"$"

    return [
        product
        for product in products
        if re.search(pattern, product, re.IGNORECASE)
    ]


# ---------------------------------------------------
# Partial keyword search
# ---------------------------------------------------
def partial_search(products, keyword):

    pattern = re.escape(keyword)

    return [
        product
        for product in products
        if re.search(pattern, product, re.IGNORECASE)
    ]


# ---------------------------------------------------
# Case-insensitive search
# ---------------------------------------------------
def case_insensitive_search(products, keyword):

    pattern = re.escape(keyword)

    return [
        product
        for product in products
        if re.search(pattern, product, re.IGNORECASE)
    ]


# ---------------------------------------------------
# Display search results
# ---------------------------------------------------
def display_results(search_type, results):

    print("\n" + "=" * 60)
    print(search_type)
    print("=" * 60)

    if results:

        for product in results:
            print(product)

    else:
        print("No matching products found.")

    print("\nTotal Matching Products:", len(results))


# ---------------------------------------------------
# Main program
# ---------------------------------------------------

products = load_products("products.txt")

if not products:
    exit()


print("=" * 60)
print("             PRODUCT SEARCH SYSTEM")
print("=" * 60)

print("\nTotal Products in Dataset:", len(products))

keyword = input("\nEnter search keyword: ").strip()

if not keyword:

    print("Error: Search keyword cannot be empty.")
    exit()


# Perform all searches
exact_results = exact_search(products, keyword)

prefix_results = prefix_search(products, keyword)

suffix_results = suffix_search(products, keyword)

partial_results = partial_search(products, keyword)

case_results = case_insensitive_search(products, keyword)


# Display results
display_results("EXACT SEARCH", exact_results)

display_results("PREFIX SEARCH", prefix_results)

display_results("SUFFIX SEARCH", suffix_results)

display_results("PARTIAL SEARCH", partial_results)

display_results("CASE-INSENSITIVE SEARCH", case_results)


# ---------------------------------------------------
# Final search report
# ---------------------------------------------------

print("\n" + "=" * 60)
print("                  SEARCH REPORT")
print("=" * 60)

print("Search Keyword          :", keyword)
print("Exact Matches           :", len(exact_results))
print("Prefix Matches          :", len(prefix_results))
print("Suffix Matches          :", len(suffix_results))
print("Partial Matches         :", len(partial_results))
print("Case-Insensitive Matches:", len(case_results))
