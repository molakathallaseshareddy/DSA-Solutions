class Solution:
    def secondLargestElement(self, nums):
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 1 or len(nums) == 0:
            return -1
        result = nums[-2]
        return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(Solution().secondLargestElement(nums))