#Solution 1
class Solution:
    def selectionSort(self, nums:list):
        result = sorted(nums)
        return result
s = Solution()
res =s.selectionSort([3,5,1,2,4])
print(res)

#Solution 2
class Solution:
    def selectionSort(self, nums:list):
        nums.sort()
        return nums
s = Solution()
res =s.selectionSort([3,5,1,2,4])
print(res)