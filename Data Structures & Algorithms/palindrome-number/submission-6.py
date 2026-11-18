class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_num = []
        num = x # shallow copy
        if x < 0:
            return False

        while num > 0:
            digit = num % 10
            num = num // 10
            rev_num.append(digit)

        as_str = ''.join(map(str, rev_num))
        return as_str == str(x) or x == 0