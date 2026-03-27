class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        realone = x
        while 0 < x:
            value = x%10
            x = x//10
            result = result * 10 + value
        if result == realone:
            return True
        else:
            return False
        