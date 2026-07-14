#Left Rotate Array by One
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
    