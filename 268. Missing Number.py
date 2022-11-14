def missingNumber(nums):
    res = len(nums)

    for i in range(len(nums)):
        print(i, nums[i])
        res += (i - nums[i])

    return res


nums = [3, 0, 1]

print(missingNumber(nums))
