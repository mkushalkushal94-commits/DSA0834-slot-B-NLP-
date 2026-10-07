def fsa_aa(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'a':
                state = 2
            else:
                state = 0

        elif state == 2:
            state = 2

    return state == 2


string = input("Enter a string: ")

if fsa_aa(string):
    print("Accepted: 'aa' is found")
else:
    print("Rejected: 'aa' is not found")
