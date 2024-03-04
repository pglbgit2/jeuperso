

TERMINAL = 0

def askFor(something:str, mod=TERMINAL):
    if mod == TERMINAL:
        return input(something)
    return ""

def throwError(someError:str, mod=TERMINAL):
    if mod == TERMINAL:
        print(someError)