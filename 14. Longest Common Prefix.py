def longestCommonPrefix(strs):
        res = ""
        minimum_length_string = min(strs, key=lambda string: len(string))
        for i in range(len(minimum_length_string)):
            for s in strs:
                if i == len(s) or s[i] != minimum_length_string[i]:
                    return res
            res += minimum_length_string[i]
        return res


print(longestCommonPrefix(["flower", "flow", "flight"]))
