class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if n==1:
            return print(n)
        print(n)
        return self.printNumbers(n-1)
if __name__ == "__main__":
    s = Solution()
    s.printNumbers(10)