### Goal is to comare two given strings when all the char's are removed with backspace -> #
### Ex: string = 'hello wor#ld' ---> Output = 'hello wold'

given_s = "ab#c"
given_t = "ad#c"

def Solution():
    new_S, new_T = [], []
    for char in given_s:
        try:
            if char != '#':
                new_S.append(char)
            else:
                new_S.pop()
        except IndexError:
            continue

    for char in given_t:
        try:
            if char != '#':
                new_T.append(char)
            else:
                new_T.pop()
        except IndexError:
            continue

    if new_T == new_S:
        return True
    else:
        return False

print(Solution())
