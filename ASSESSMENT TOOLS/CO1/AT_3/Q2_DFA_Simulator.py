import re


# --------------------------------------------------
# Read DFA description from file
# --------------------------------------------------
def load_dfa(filename):

    try:
        with open(filename, "r") as file:
            data = file.read()

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    lines = [
        line.strip()
        for line in data.splitlines()
        if line.strip()
    ]

    states = []
    alphabet = []
    start_state = ""
    final_states = []
    transitions = {}
    input_strings = []

    transition_section = False
    string_section = False

    for line in lines:

        if line.startswith("STATES:"):

            states = [
                state.strip()
                for state in line.split(":", 1)[1].split(",")
            ]

            continue

        if line.startswith("ALPHABET:"):

            alphabet = [
                symbol.strip()
                for symbol in line.split(":", 1)[1].split(",")
            ]

            continue

        if line.startswith("START:"):

            start_state = line.split(":", 1)[1].strip()

            continue

        if line.startswith("FINAL:"):

            final_states = [
                state.strip()
                for state in line.split(":", 1)[1].split(",")
            ]

            continue

        if line == "TRANSITIONS:":
            transition_section = True
            string_section = False
            continue

        if line == "STRINGS:":
            transition_section = False
            string_section = True
            continue

        if transition_section:

            parts = [
                part.strip()
                for part in line.split(",")
            ]

            if len(parts) == 3:

                current_state = parts[0]
                symbol = parts[1]
                next_state = parts[2]

                transitions[
                    (current_state, symbol)
                ] = next_state

        elif string_section:

            input_strings.append(line)

    return {
        "states": states,
        "alphabet": alphabet,
        "start": start_state,
        "final": final_states,
        "transitions": transitions,
        "strings": input_strings
    }


# --------------------------------------------------
# Validate DFA
# --------------------------------------------------
def validate_dfa(dfa):

    if not dfa["states"]:
        return False, "No states defined."

    if not dfa["alphabet"]:
        return False, "No alphabet defined."

    if dfa["start"] not in dfa["states"]:
        return False, "Invalid start state."

    for state in dfa["final"]:

        if state not in dfa["states"]:
            return False, f"Invalid final state: {state}"

    for state in dfa["states"]:

        for symbol in dfa["alphabet"]:

            if (state, symbol) not in dfa["transitions"]:

                return False, (
                    f"Missing transition for "
                    f"{state} with {symbol}"
                )

            next_state = dfa["transitions"][
                (state, symbol)
            ]

            if next_state not in dfa["states"]:

                return False, (
                    f"Invalid destination state: "
                    f"{next_state}"
                )

    return True, "Valid DFA"


# --------------------------------------------------
# Simulate input string
# --------------------------------------------------
def simulate(dfa, input_string):

    current_state = dfa["start"]

    path = [current_state]

    for symbol in input_string:

        if symbol not in dfa["alphabet"]:

            return (
                False,
                path,
                f"Invalid input symbol '{symbol}'"
            )

        current_state = dfa["transitions"][
            (current_state, symbol)
        ]

        path.append(current_state)

    accepted = current_state in dfa["final"]

    return accepted, path, None


# --------------------------------------------------
# Main Program
# --------------------------------------------------

dfa = load_dfa("Q2_dfa_input.txt")

if dfa is None:
    exit()


valid, message = validate_dfa(dfa)

if not valid:

    print("DFA Error:", message)
    exit()


print("=" * 70)
print("                     DFA SIMULATOR")
print("=" * 70)

print("\nStates       :", ", ".join(dfa["states"]))
print("Alphabet     :", ", ".join(dfa["alphabet"]))
print("Initial State:", dfa["start"])
print("Final States :", ", ".join(dfa["final"]))


print("\nTransition Table")
print("-" * 50)

print(
    f"{'State':<15}"
    f"{'a':<15}"
    f"{'b':<15}"
)

for state in dfa["states"]:

    a_next = dfa["transitions"].get(
        (state, "a"),
        "-"
    )

    b_next = dfa["transitions"].get(
        (state, "b"),
        "-"
    )

    print(
        f"{state:<15}"
        f"{a_next:<15}"
        f"{b_next:<15}"
    )


print("\n" + "=" * 70)
print("                  STRING PROCESSING")
print("=" * 70)


accepted_count = 0
rejected_count = 0


for number, input_string in enumerate(
    dfa["strings"],
    start=1
):

    accepted, path, error = simulate(
        dfa,
        input_string
    )

    print(f"\nInput String {number}: {input_string}")

    print(
        "Transition Path:",
        " → ".join(path)
    )

    if error:

        print("Result:", error)
        print("Status: REJECTED")

        rejected_count += 1

    elif accepted:

        print("Status: ACCEPTED")

        accepted_count += 1

    else:

        print("Status: REJECTED")

        rejected_count += 1


print("\n" + "=" * 70)
print("                     FINAL REPORT")
print("=" * 70)

print("Total Strings :", len(dfa["strings"]))
print("Accepted      :", accepted_count)
print("Rejected      :", rejected_count)
