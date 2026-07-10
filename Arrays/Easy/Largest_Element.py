#Largest Element Finding
class Solution:
    def largestElement(self, nums):
        value = nums[0]
        for i in nums:
            if i > value:
                value = i
        return value
if __name__ == "__main__":
    s = Solution()
    result = s.largestElement([3, 3, 0, 99, -40])
    print(result)