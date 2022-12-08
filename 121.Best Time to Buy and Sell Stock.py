from itertools import accumulate

def maxProfit(prices):
    l = 0
    r = 1
    max_value = 0

    while len(prices) > r > l:
        if prices[r] < prices[l]:
            l = r
            r += 1
        else:
            if prices[r] - prices[l] > max_value:
                max_value = prices[r] - prices[l]
            r += 1
    return max_value


prices = [1, 2, 1, 0, 1, 2]
ls = accumulate(prices)
print(list(ls))

