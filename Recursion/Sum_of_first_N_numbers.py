class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        if N==0:
            return 0
        return N +self.NnumbersSum(N-1)
if __name__ == "__main__":
    result = Solution().NnumbersSum(5)
    print(result)