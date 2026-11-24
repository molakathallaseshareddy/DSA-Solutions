class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if n==1:
            return print(n)
        print(n)
        self.printNumbers(n-1)
if __name__ == "__main__":
    s = Solution()
    s.printNumbers(10)
    
class Solution:
    def printNumbers(self, n):
        # Your code goes here
        print(n)
        if n==1:
            return
        self.printNumbers(n-1)
if __name__ == "__main__":
    s = Solution()
    s.printNumbers(10)