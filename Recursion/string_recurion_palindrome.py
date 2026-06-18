class Solution:    
    def palindromeCheck(self, s, n:int):
        if n ==0:
            return s[n]
        p = s[n-1]+self.palindromeCheck(s, n-1)
        if p == s:
            return True
        else:
            return False
