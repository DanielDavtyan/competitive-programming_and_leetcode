# Solution O(n ^ 3) brute force
def longestPalindrome_brute_force(s: str):
    list_of_substrings = []
    for j in range(len(s)):
        current_substring = ''
        for i in range(len(s)):
            if i + j < len(s):
                current_substring += s[i + j]
            if current_substring == current_substring[::-1]:
                list_of_substrings.append(current_substring)
    substring_array = sorted(list_of_substrings, key=lambda p: len(p))
    return substring_array[-1]


# Solution O(n ^ 2)
def longestPalindrome(s):
    res = ""
    resLen = 0
    for i in range(len(s)):
        l, r = i, i
        # odd length
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if resLen < (r - l + 1):
                res = s[l:r + 1]
                resLen = r - l + 1
            r += 1
            l -= 1
        # even length
        l, r = i, i + 1
        while l >= 0 and r <= len(s) and s[l] == s[r]:
            if resLen < (r - l + 1):
                res = s[l:r + 1]
                resLen = r - l + 1
            r += 1
            l -= 1
    return res
s = "babad"
print(longestPalindrome(s))
