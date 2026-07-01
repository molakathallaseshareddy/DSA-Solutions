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