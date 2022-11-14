def myAtoi(s: str) -> int:
    MIN = -2147483648
    MAX = 2147483647
    counter = 0
    sign = False
    result_number = ""
    for char in s:
        if char == " ":
            continue
        elif char == "-":
            sign = True
            counter += 1
        elif char == "+":
            counter += 1
            continue
        elif char.isdigit():
            result_number += char
        else:
            break
    if sign:
        if len(result_number) == 0 or counter > 1:
            return 0
        elif len(result_number) and MIN <= int(result_number) <= MAX:
            return -1 * int(result_number)
        elif -1 * int(result_number) > MAX:
            return MAX
        else:
            return MIN
    else:
        if len(result_number) == 0 or counter > 1:
            return 0
        elif len(result_number) and MIN <= int(result_number) <= MAX:
            return int(result_number)
        elif int(result_number) > MAX:
            return MAX
        else:
            return MIN


def myAtoi2(s):
    MIN = -2147483648
    MAX = 2147483647
    s = s.lstrip()

    if not s:
        return 0
    i = 0
    sign = 1
    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        i += 1
        sign = -1

    parsed = 0
    while i < len(s):
        cur = s[i]
        if not cur.isdigit():
            break
        else:
            parsed = parsed * 10 + int(cur)
        i += 1

    parsed *= sign

    if parsed > 2**31 - 1:
        return 2**31 - 1
    elif parsed <= -2**31 - 1:
        return -2 ** 31
    else:
        return parsed

print(myAtoi("42"))
