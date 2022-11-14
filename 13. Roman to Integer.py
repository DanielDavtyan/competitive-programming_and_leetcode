def romanToInt(s):
    mapping_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    res = 0
    for i in range(len(s)):
        if (i + 1 < len(s)) and mapping_dict[s[i]] < mapping_dict[s[i + 1]]:
            res -= mapping_dict[s[i]]
        else:
            res += mapping_dict[s[i]]
    return res
