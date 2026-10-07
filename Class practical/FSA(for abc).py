def fsa_abc(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if ch == 'c':
                state = 3
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 3:
            state = 3

    return state == 3


string = input("Enter a string: ")

if fsa_abc(string):
    print("Accepted: 'abc' is found")
else:
    print("Rejected: 'abc' is not found")
