# First Solution
# this is not recursive solution, normal solution for fibonacci number
class Solution:
    def fib(self, n):
        #your code goes here
        a = 0
        b = 1
        if n == a:
            return a
        if n == b:
            return b
        res = 0
        for i in range(1, n+1):
            if i == n:
                res = a+b
                return res
            res = a+b
            print(res)
            b = a
            a = res
if __name__ == "__main__":
    s = Solution()
    result = s.fib(5)
    print(result)

# Second Solution
# recursive solution for fibonacci number
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n ==1:
            return 1
        def help(i, a, b):
            if n == i:
                return b
            return help(i+1, b, a+b)
        return help(1,0,1)