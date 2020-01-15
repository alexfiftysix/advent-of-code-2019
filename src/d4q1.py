PASSWORD_LENGTH = 6


def check_length(p: int):
    return len(f'{p}') == PASSWORD_LENGTH


def check_double(p: int):
    p = str(p)
    for i in range(len(p) - 1):
        if p[i] == p[i + 1]:
            return True
    return False


def check_ascending(p: int):
    p = str(p)
    for i in range(len(p) - 1):
        if int(p[i + 1]) < int(p[i]):
            return False
    return True


def validate_password(p: int):
    return check_length(p) and check_double(p) and check_ascending(p)


if __name__ == '__main__':
    count = 0
    for x in range(206938, 679128 + 1):
        if validate_password(x):
            count += 1
    print(count)
