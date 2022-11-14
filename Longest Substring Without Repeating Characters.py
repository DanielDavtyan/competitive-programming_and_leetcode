def lengthOfLongestSubstring(s: str) -> int:
    if not len(s):
        return 0
    if len(list(set(s))) == 1:
        return 1
    current_substring = ''
    substring_array = []
    for j in range(len(s)):
        for i in range(len(s)):
            if i + j < len(s):
                current_substring += s[i + j]
                if current_substring.count(s[i + j]) > 1:
                    substring_array.append(current_substring)
                    current_substring = ''
                    break
    max_substring = max(substring_array, key=lambda p: len(p))
    return len(max_substring) - 1

str1 = "asanfbgfdhdh"
print(lengthOfLongestSubstring(str1))
