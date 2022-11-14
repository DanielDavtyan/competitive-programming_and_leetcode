def findDisappearedNumbers(nums):
    hash_set = {}
    res = set()
    for i in range(1, len(nums) + 1):
        hash_set[i] = 0
    for i in nums:
        hash_set[i] += 1
    for k in hash_set.keys():
        if hash_set[k] == 0:
            res.add(k)
    return res


# second solution
def findDisappearedNumbers_2(nums):
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])

    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i + 1)
    return res


nums = [1, 1]

print(findDisappearedNumbers_2(nums))
