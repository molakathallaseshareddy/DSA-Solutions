#First Solution
class Solution:    
    def palindromeCheck(self, s, n:int):
        if n ==0:
            return s[n]
        p = s[n-1]+self.palindromeCheck(s, n-1)
        if p == s:
            return True
        else:
            return False


# Second Solution
class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        n = len(s)
        def help(n):
            if n == 1:
                return s[n-1]
            return s[n-1] + help(n-1)
        a = help(n)
        if s == a:
            return True
        else:
            return False
if __name__ == "__main__":
    s = Solution()
    result = s.palindromeCheck("madam")
    print(result)