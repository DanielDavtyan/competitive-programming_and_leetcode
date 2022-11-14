# Dynamic programming approach (top to down)

def isMatch(s: str, p: str):
    cache = {}

    def match_checker(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        if i >= len(s) and j >= len(p):
            cache[(i, j)] = True
            return True
        if j >= len(p):
            cache[(i, j)] = False
            return False
        if i >= len(s):
            if len(p) > j + 1 and p[j + 1] == "*":
                cache[(i, j)] = match_checker(i, j + 2)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        match = (s[i] == p[j] or p[j] == '.')
        if not match:
            if len(p) > j + 1 and p[j + 1] == "*":
                cache[(i, j)] = match_checker(i, j + 2)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False
        elif len(p) <= j + 1 or p[j + 1] != "*":
            cache[(i, j)] = match_checker(i + 1, j + 1)
            return cache[(i, j)]
        else:
            cache[(i, j)] = match_checker(i + 1, j) or match_checker(i, j + 2)
            return cache[(i, j)]

    return match_checker(0, 0)


print(isMatch("aab", "c*a*b"))
