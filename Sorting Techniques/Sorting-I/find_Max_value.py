class Solution:
    def findMaxvalue(self, nums):
        max_value = nums[0]
        for value in nums:
            if max_value < value:
                max_value = value
                continue
        return max_value
if __name__ == "__main__":
    s = Solution()
    print(s.findMaxvalue([4,5,2,3,1,6,8,7]))
            