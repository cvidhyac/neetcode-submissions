class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_copy = x
        reversed_num = 0
        while num_copy > 0:
            digit = num_copy % 10
            num_copy = num_copy // 10
            reversed_num = (reversed_num * 10) + digit
        return x == reversed_num
