class Solution:
    def bubbleSort(self, nums:list):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
if __name__ == "__main__":
    s = Solution()
    print(s.bubbleSort([3,2,7,5,1]))
