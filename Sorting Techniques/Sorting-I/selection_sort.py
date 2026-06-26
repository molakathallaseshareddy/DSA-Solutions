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

#Solution 3
class Solution:
    def selectionSort(self, nums):
        result = []
        def help(nums):
            a = nums[0]
            for i in nums:
                if a>i:
                    a = i
                    continue
            result.append(a)
            nums.remove(a)
            if len(nums) == 0:
                return
            help(nums)
        help(nums)
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.selectionSort([4,5,2,3,1]))
            