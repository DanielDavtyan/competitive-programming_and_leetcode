def twoSum(nums, target: int):
    l = {}
    for i in range(len(nums)):
        if target - nums[i] in l:
            return [i, l[target - nums[i]]]
        else:
            l[nums[i]] = i


ls = [2, 11, 7, 15]

twoSum(ls, 9)