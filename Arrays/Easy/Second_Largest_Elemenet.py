class Solution:
    def secondLargestElement(self, nums):
        nums = list(set(nums))
        nums.sort()
        result = nums[-2]
        return result

print(Solution().secondLargestElement([1, 2, 3, 4, 5]))