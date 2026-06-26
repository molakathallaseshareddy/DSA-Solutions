class Solution:
    def findMinvalue(self, nums):
        result = []
        a = nums[0]
        for i in nums:
            if a>i:
                a = i
                continue
        return a
if __name__ == "__main__":
    s = Solution()
    print(s.findMinvalue([4,5,2,3,1,6,8,7]))
            