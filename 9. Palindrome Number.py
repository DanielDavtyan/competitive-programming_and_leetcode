def isPalindrome(x: int) -> bool:
    reversed_number = 0
    if x < 0: return False

    current_number = x
    while x != 0:
        curr_digit = x % 10
        x //= 10
        reversed_number = (10 * reversed_number) + curr_digit
    return current_number == reversed_number


print(isPalindrome(152))
