# #Left Rotate Array by One
# solution 1
class Solution:
    def rotateArrayByOne(self, nums):
        value = nums[0]
        nums.pop(0)
        nums.append(value)
        return nums

if __name__ == "__main__":
    s = Solution()
    result = s.leftRotateArrayByOne([1, 2, 3, 4, 5])
    print(result)

# solytion 2
# Left Rotate Array by One
class Solution:
    def rotateArrayByOne(self, nums):
        first_element = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[-1] = first_element
        return nums
