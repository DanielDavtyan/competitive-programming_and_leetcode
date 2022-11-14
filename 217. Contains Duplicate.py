def containsDuplicate(nums):
    counter_dict = {}
    for i in nums:
        counter_dict[i] = 0
    for i in nums:
        counter_dict[i] += 1
        if counter_dict[i] > 1:
            return True
    return False


nums = [1, 2, 3, 1]

print(containsDuplicate(nums))
