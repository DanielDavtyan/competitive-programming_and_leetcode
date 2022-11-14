# O(n)

def maxArea(heigh):
    result = 0
    i = 0
    j = len(heigh) - 1
    while i < j:
        minimum = min(heigh[i], heigh[j])
        current_result = (j - i) * minimum
        result = max(result, current_result)
        if heigh[i] == minimum:
            i += 1
        elif heigh[j] == minimum:
            j -= 1
    return result


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
