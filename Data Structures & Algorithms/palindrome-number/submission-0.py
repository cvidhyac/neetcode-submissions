class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        if x < 0:
         return False
        num_copy = x 
        while num_copy > 0:
         digit = num_copy % 10
         num_copy = num_copy // 10
         reversed_num = (reversed_num * 10) + digit
        if x == reversed_num:
            return True
        return False