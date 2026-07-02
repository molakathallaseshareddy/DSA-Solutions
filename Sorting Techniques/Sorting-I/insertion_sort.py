class Solution:
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums
if __name__ == "__main__":
    s = Solution()
    print(s.insertionSort([3,2,7,5,1]))

#Insertion Sort second solution
class Solution:
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            for j in range(i+1,-1,-1):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
if __name__ == "__main__":
    s = Solution()
    print(s.insertionSort([3,2,1,4,8,6]))