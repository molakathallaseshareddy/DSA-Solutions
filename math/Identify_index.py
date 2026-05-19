class Solution:
    def search(self, nums, target):
        for i in nums:
            if i == target:
                result = nums.index(i)
                return result
if __name__ == "__main__":
    a = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(a.search(nums, target))